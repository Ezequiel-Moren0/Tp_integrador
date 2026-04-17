from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, strict=True)
    email: EmailStr
    activo: bool = True

    @validator("nombre")
    def nombre_valido(cls, v):
        if not v.strip():
            raise ValueError("El nombre no puede contener solo espacios")
        if any(char.isdigit() for char in v):
            raise ValueError("El nombre no puede contener números")
        return v.strip().title()

class ClienteCreate(ClienteBase):
    email: EmailStr = Field(..., description="Email único del cliente")
    activo: bool = Field(default=True)

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True