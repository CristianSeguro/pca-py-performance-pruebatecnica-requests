"""
Mock API Server para pruebas con FastAPI
========================================

Este servidor mock simula una API REST real usando FastAPI para que puedas probar
las funciones de requests sin depender de servicios externos.

Para ejecutar:
    python mock_api_server_fastapi.py
    
    O usando uvicorn directamente:
    uvicorn mock_api_server_fastapi:app --reload --host 0.0.0.0 --port 8000

El servidor estará disponible en: http://localhost:8000
Documentación automática: http://localhost:8000/docs
Documentación alternativa: http://localhost:8000/redoc

Ventajas de FastAPI:
- Documentación automática interactiva (Swagger UI)
- Validación automática de datos con Pydantic
- Mejor rendimiento que Flask
- Type hints nativos
- Async/await support
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Importar los endpoints
from endpoints.usuarios_endpoint import UsuariosEndPoint
from endpoints.autenticacion_endpoint import AutenticacionEndPoint
from endpoints.testing_endpoint import TestingEndPoint
from endpoints.sistema_endpoint import SistemaEndPoint

# Crear la aplicación FastAPI
app = FastAPI(
    title="Mock API Server",
    description="Servidor mock para pruebas de la librería requests",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    tags_metadata=[
        {
            "name": "Usuarios",
            "description": "Operaciones CRUD para gestión de usuarios"
        },
        {
            "name": "Autenticación", 
            "description": "Endpoints de autenticación y autorización"
        },
        {
            "name": "Testing",
            "description": "Endpoints para probar diferentes escenarios (errores, timeouts, etc.)"
        },
        {
            "name": "Sistema",
            "description": "Información del sistema y health checks"
        }
    ]
)

# Incluir los routers con sus prefijos y tags
app.include_router(UsuariosEndPoint.usuarios_router, prefix="/users", tags=["Usuarios"])
app.include_router(AutenticacionEndPoint.autenticacion_router, prefix="/autenticacion", tags=["Autenticación"])
app.include_router(TestingEndPoint.testing_router, prefix="/testing", tags=["Testing"])
app.include_router(SistemaEndPoint.sistema_router, prefix="/sistema", tags=["Sistema"])

# Endpoint raíz adicional (fuera de los routers)
@app.get("/", tags=["Sistema"])
async def root():
    """Endpoint raíz con información del API"""
    return {
        "message": "API Server Prueba Siste",
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "health_check": "/sistema/health"
    }


# === MANEJADORES DE ERRORES PERSONALIZADOS ===

@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": "Endpoint not found", "detail": str(exc)}
    )


@app.exception_handler(422)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"error": "Validation error", "detail": str(exc)}
    )


# === FUNCIÓN PRINCIPAL ===

if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Iniciando Mock API Server con FastAPI...")
    print("📡 Servidor disponible en: http://localhost:8000")
    print("📖 Documentación Swagger: http://localhost:8000/docs")
    print("📚 Documentación ReDoc: http://localhost:8000/redoc")
    print("🔍 Health Check: http://localhost:8000/health")
    print("🛑 Para detener: Ctrl+C")
    print("-" * 60)
    
    # Configuración para desarrollo
    uvicorn.run(
        "mock_api_server_fastapi:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Recarga automática en desarrollo
        log_level="info"
    )
