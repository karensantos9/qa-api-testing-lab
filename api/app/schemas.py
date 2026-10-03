from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    password: str = Field(min_length=6)
    role: Literal["user", "admin"] = "user"


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    role: Literal["user", "admin"]