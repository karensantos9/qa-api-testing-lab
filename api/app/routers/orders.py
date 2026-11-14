
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Order, OrderItem, Product, User
from ..schemas import OrderCreate, OrderUpdate, OrderResponse
from .auth import get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


def validate_order_items(db, items, previous_quantities=None):
    """
    Valida os produtos, as quantidades e o estoque disponível.
    previous_quantities é utilizado durante a atualização do pedido.
    """

    if previous_quantities is None:
        previous_quantities = {}

    validated_items = []
    seen_products = set()

    for item in items:
        product_id = item.product_id
        quantity = item.quantity

        if product_id in seen_products:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Duplicate products are not allowed in the same order"
            )

        seen_products.add(product_id)

        product = db.query(Product).filter(
            Product.id == product_id
        ).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product {product_id} not found"
            )

        available_stock = (
            product.stock + previous_quantities.get(product_id, 0)
        )

        if quantity > available_stock:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product_id}"
            )

        validated_items.append((product, quantity))

    return validated_items


@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    validated_items = validate_order_items(
        db,
        order_data.items
    )

    total = sum(
        product.price * quantity
        for product, quantity in validated_items
    )

    new_order = Order(
        user_id=current_user.id,
        total=round(total, 2)
    )

    db.add(new_order)
    db.flush()

    for product, quantity in validated_items:
        subtotal = round(product.price * quantity, 2)

        order_item = OrderItem(
            order_id=new_order.id,
            product_id=product.id,
            quantity=quantity,
            unit_price=product.price,
            subtotal=subtotal
        )

        db.add(order_item)

        product.stock -= quantity

    db.commit()
    db.refresh(new_order)

    return new_order


@router.get(
    "",
    response_model=list[OrderResponse]
)
def list_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    orders = db.query(Order).filter(
        Order.user_id == current_user.id
    ).all()

    return orders


@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    return order


@router.put(
    "/{order_id}",
    response_model=OrderResponse
)
def update_order(
    order_id: int,
    order_data: OrderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    # Guarda as quantidades anteriores para recalcular
    # corretamente o estoque disponível.
    previous_quantities = {}

    for item in order.items:
        previous_quantities[item.product_id] = (
            previous_quantities.get(item.product_id, 0)
            + item.quantity
        )

    # Valida todos os novos itens antes de modificar o pedido.
    validated_items = validate_order_items(
        db,
        order_data.items,
        previous_quantities
    )

    # Devolve ao estoque as quantidades do pedido anterior.
    for product_id, quantity in previous_quantities.items():
        product = db.query(Product).filter(
            Product.id == product_id
        ).first()

        if product:
            product.stock += quantity

    # Remove os itens antigos.
    for old_item in list(order.items):
        db.delete(old_item)

    # Cria os novos itens e desconta o estoque.
    new_total = 0

    for product, quantity in validated_items:
        subtotal = round(product.price * quantity, 2)
        new_total += subtotal

        new_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=quantity,
            unit_price=product.price,
            subtotal=subtotal
        )

        db.add(new_item)
        product.stock -= quantity

    order.total = round(new_total, 2)

    db.commit()
    db.refresh(order)

    return order


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )

    # Devolve ao estoque os produtos do pedido.
    for item in order.items:
        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()

        if product:
            product.stock += item.quantity

    db.delete(order)
    db.commit()

    return None
