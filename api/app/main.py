
from fastapi import FastAPI

from .database import Base, engine
from .routers import users, products, auth, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sales API",
    description="API de vendas para laboratório de testes de QA",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(orders.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
