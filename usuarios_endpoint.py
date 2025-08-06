"""
Endpoints para la gestión de usuarios
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any, List


# Esquemas de datos
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class UsuariosEndPoint:
    
    usuarios_router = APIRouter()
    
    # Datos de ejemplo (simulando una base de datos)
    users_db = [
        {"id": 1, "name": "Juan Pérez", "email": "juan@example.com"},
        {"id": 2, "name": "María García", "email": "maria@example.com"},
        {"id": 3, "name": "Carlos López", "email": "carlos@example.com"}
    ]
    
    @usuarios_router.get("/", 
                        response_model=Dict[str, Any],
                        summary="Obtener lista de usuarios",
                        description="Obtiene la lista de usuarios con paginación opcional")
    async def get_users(page: int = 1, limit: int = 10):
        """GET /users - Obtener usuarios con paginación"""
        start = (page - 1) * limit
        end = start + limit
        
        return {
            "users": UsuariosEndPoint.users_db[start:end],
            "page": page,
            "limit": limit,
            "total": len(UsuariosEndPoint.users_db)
        }

    @usuarios_router.get("/{user_id}", 
                        response_model=Dict[str, Any],
                        summary="Obtener usuario específico",
                        description="Obtiene un usuario por su ID")
    async def get_user(user_id: int):
        """GET /users/{id} - Obtener usuario específico"""
        user = next((u for u in UsuariosEndPoint.users_db if u["id"] == user_id), None)
        if user:
            return user
        
        raise HTTPException(status_code=404, detail="User not found")

    @usuarios_router.post("/", 
                         response_model=Dict[str, Any],
                         status_code=201,
                         summary="Crear nuevo usuario",
                         description="Crea un nuevo usuario con los datos proporcionados")
    async def create_user(user: User):
        """POST /users - Crear nuevo usuario"""
        new_user = {
            "id": len(UsuariosEndPoint.users_db) + 1,
            "name": user.name,
            "email": user.email
        }
        UsuariosEndPoint.users_db.append(new_user)
        
        return new_user

    @usuarios_router.put("/{user_id}", 
                        response_model=Dict[str, Any],
                        summary="Actualizar usuario",
                        description="Actualiza los datos de un usuario existente")
    async def update_user(user_id: int, user_update: UserUpdate):
        """PUT /users/{id} - Actualizar usuario"""
        user = next((u for u in UsuariosEndPoint.users_db if u["id"] == user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Actualizar solo los campos proporcionados
        if user_update.name is not None:
            user["name"] = user_update.name
        if user_update.email is not None:
            user["email"] = user_update.email
        
        return user

    @usuarios_router.delete("/{user_id}", 
                           status_code=204,
                           summary="Eliminar usuario",
                           description="Elimina un usuario por su ID")
    async def delete_user(user_id: int):
        """DELETE /users/{id} - Eliminar usuario"""
        user = next((u for u in UsuariosEndPoint.users_db if u["id"] == user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        UsuariosEndPoint.users_db = [u for u in UsuariosEndPoint.users_db if u["id"] != user_id]
        return  # 204 No Content
