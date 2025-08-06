"""
Endpoints para información del sistema
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any
import time


# Esquemas de datos
class HealthResponse(BaseModel):
    status: str
    timestamp: float
    endpoints: List[str]


class SistemaEndPoint:
    
    sistema_router = APIRouter()

    @sistema_router.get("/health", 
                       response_model=HealthResponse,
                       summary="Health Check",
                       description="Endpoint de estado del servidor y lista de endpoints disponibles")
    async def health_check():
        """GET /health - Health check endpoint"""
        return HealthResponse(
            status="healthy",
            timestamp=time.time(),
            endpoints=[
                "GET /users - Lista usuarios con paginación",
                "GET /users/{id} - Usuario específico",
                "POST /users - Crear usuario",
                "PUT /users/{id} - Actualizar usuario", 
                "DELETE /users/{id} - Eliminar usuario",
                "POST /autenticacion/login - Login con form data",
                "GET /autenticacion/secure - Headers personalizados",
                "GET /autenticacion/bearer - Autenticación Bearer",
                "GET /autenticacion/basic-auth - Autenticación básica",
                "GET /testing/slow?delay=N - Endpoint lento",
                "GET /testing/error/{status} - Generar errores",
                "GET /testing/random-error - Error aleatorio",
                "GET /docs - Documentación Swagger UI",
                "GET /redoc - Documentación ReDoc"
            ]
        )

    @sistema_router.get("/", 
                       summary="Página de inicio",
                       description="Información básica del API")
    async def root():
        """Endpoint raíz con información del API"""
        return {
            "message": "Mock API Server con FastAPI",
            "version": "1.0.0",
            "docs_url": "/docs",
            "redoc_url": "/redoc",
            "health_check": "/sistema/health"
        }
