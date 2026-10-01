from fastapi import FastAPI

from .database import Base, engine
from .routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sales API",
    description="API de vendas para laboratório de testes de QA",
    version="1.0.0"
)

app.include_router(users.router)


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }