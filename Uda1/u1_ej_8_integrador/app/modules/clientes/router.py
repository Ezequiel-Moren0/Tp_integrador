from fastapi import APIRouter, Query
from typing import Optional
from app.modules.clientes import service
from app.modules.clientes.schemas import ClienteCreate, ClienteResponse

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.get("/", response_model=list[ClienteResponse])
def get_clientes(
    nombre: Optional[str] = Query(default=None, description="Filtrar por nombre"),
    email: Optional[str] = Query(default=None, description="Filtrar por email"),
    activo: Optional[bool] = Query(default=None, description="Filtrar por estado activo/inactivo"),
):
    return service.filtrar_clientes(nombre=nombre, email=email, activo=activo)


@router.get("/{cliente_id}", response_model=ClienteResponse)
def get_cliente(cliente_id: int):
    return service.get_cliente_activo(cliente_id)


@router.post("/", response_model=ClienteResponse, status_code=201)
def crear_cliente(cliente: ClienteCreate):
    return service.crear_cliente(cliente)