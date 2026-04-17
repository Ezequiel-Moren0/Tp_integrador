from typing import Optional
from fastapi import HTTPException

clientes_base_de_datos = [
    {"id": 1, "nombre": "Pepe Argento", "email": "pepe@gmail.com", "activo": True},
    {"id": 2, "nombre": "Luz Marina", "email": "luz@gmail.com", "activo": False},
    {"id": 3, "nombre": "Juan Roman Riquelme", "email": "juan@gmail.com", "activo": True}
]

#Profe las reglas que voy a usar son:
#Regla 1: El limite para crear clientes es de 10
#Regla 2: No se pueden repetir los mails
#Regla 3: Un cliente inactivo no puede ser consultado en ciertas operaciones

MIN_CLIENTES = 10

def filtrar_clientes(
    nombre: Optional[str] = None,
    email: Optional[str] = None,
    activo: Optional[bool] = None,
):
    resultado = clientes_base_de_datos

    if nombre:
        resultado = [c for c in resultado if nombre.lower() in c["nombre"].lower()]

    if email:
        resultado = [c for c in resultado if email.lower() in c["email"].lower()]

    if activo is not None:
        resultado = [c for c in resultado if c["activo"] == activo]

    return resultado

def crear_cliente(cliente):
    if len(clientes_base_de_datos) >= MIN_CLIENTES:
        raise HTTPException(status_code=400, detail="Supero el limite de clientes")
    
    if any(c["email"] == cliente.email for c in clientes_base_de_datos):
        raise HTTPException(status_code=400, detail="El email ya esta en uso")
    

    nuevo = {"id": len(clientes_base_de_datos) + 1, "nombre": cliente.nombre, "email": cliente.email, "activo": cliente.activo}
    clientes_base_de_datos.append(nuevo)
    return nuevo

def get_cliente_activo(cliente_id: int):
    cliente = next((c for c in clientes_base_de_datos if c["id"] == cliente_id), None)

    if not cliente:
        raise HTTPException(status_code=404, detail="No se encontro el cliente")
    if not cliente["activo"]:
        raise HTTPException(status_code=403, detail="El cliente está inactivo y no puede ser consultado")

    return cliente