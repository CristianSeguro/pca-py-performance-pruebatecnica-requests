"""
Endpoints para testing y pruebas
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import asyncio
import random


class TestingEndPoint:
    
    testing_router = APIRouter()

    @testing_router.get("/slow", 
                       response_model=Dict[str, Any],
                       summary="Endpoint lento",
                       description="Endpoint que simula respuesta lenta para probar timeouts")
    async def slow_endpoint(delay: int = 3):
        """GET /slow - Endpoint que tarda en responder (para timeout)"""
        await asyncio.sleep(delay)
        return {"data": "slow response", "delay": delay}

    @testing_router.get("/error/{status_code}", 
                       summary="Generar errores HTTP",
                       description="Endpoint que retorna diferentes códigos de estado HTTP")
    async def error_endpoint(status_code: int):
        """GET /error/{status} - Endpoint que retorna diferentes errores"""
        error_messages = {
            400: "Bad Request",
            401: "Unauthorized", 
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error",
            502: "Bad Gateway",
            503: "Service Unavailable"
        }
        
        message = error_messages.get(status_code, f"Error {status_code}")
        
        raise HTTPException(status_code=status_code, detail=message)

    @testing_router.get("/random-error", 
                       response_model=Dict[str, Any],
                       summary="Error aleatorio",
                       description="Endpoint que falla aleatoriamente (30% probabilidad)")
    async def random_error():
        """GET /random-error - Endpoint que a veces falla"""
        if random.random() < 0.3:  # 30% de probabilidad de error
            raise HTTPException(status_code=500, detail="Random failure")
        
        return {"data": "success"}
