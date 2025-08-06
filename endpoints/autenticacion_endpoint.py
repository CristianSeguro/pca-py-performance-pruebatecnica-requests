"""
Endpoints para autenticación y autorización
"""

from fastapi import APIRouter, HTTPException, Depends, status, Form, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional, Dict, Any


# Esquemas de datos
class LoginResponse(BaseModel):
    success: bool
    message: str
    token: Optional[str] = None

class AuthResponse(BaseModel):
    user: str
    token: Optional[str] = None
    status: Optional[str] = None


# Simulación de autenticación
valid_tokens = ["abc123token", "token456", "secrettoken"]
valid_users = {"admin": "password", "user": "123456"}

# Configuración de seguridad
security_basic = HTTPBasic()
security_bearer = HTTPBearer()


def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security_basic)):
    """Verificar autenticación básica"""
    username = credentials.username
    password = credentials.password
    
    if username not in valid_users or valid_users[username] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return username


def verify_bearer_token(credentials: HTTPAuthorizationCredentials = Depends(security_bearer)):
    """Verificar Bearer token"""
    token = credentials.credentials
    if token not in valid_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


class AutenticacionEndPoint:
    
    autenticacion_router = APIRouter()

    @autenticacion_router.post("/login", 
                              response_model=LoginResponse,
                              summary="Login con credenciales",
                              description="Autenticación usando form data (application/x-www-form-urlencoded)")
    async def login(username: str = Form(...), password: str = Form(...)):
        """POST /login - Login con form data"""
        if username in valid_users and valid_users[username] == password:
            return LoginResponse(
                success=True,
                message="Login successful",
                token="abc123token"
            )
        
        raise HTTPException(
            status_code=401, 
            detail=LoginResponse(success=False, message="Invalid credentials").dict()
        )

    @autenticacion_router.get("/secure", 
                             response_model=Dict[str, Any],
                             summary="Endpoint con headers personalizados",
                             description="Endpoint que retorna información sobre los headers recibidos")
    async def secure_endpoint(
        user_agent: Optional[str] = Header(None),
        accept: Optional[str] = Header(None),
        x_custom_header: Optional[str] = Header(None)
    ):
        """GET /secure - Endpoint que requiere headers personalizados"""
        return {
            "data": "secured",
            "headers_received": {
                "User-Agent": user_agent,
                "Accept": accept,
                "X-Custom-Header": x_custom_header
            }
        }

    @autenticacion_router.get("/bearer", 
                             response_model=AuthResponse,
                             summary="Autenticación Bearer Token",
                             description="Endpoint protegido con Bearer Token")
    async def bearer_auth(token: str = Depends(verify_bearer_token)):
        """GET /bearer - Endpoint con autenticación Bearer"""
        return AuthResponse(user="authenticated", token=token)

    @autenticacion_router.get("/basic-auth", 
                             response_model=AuthResponse,
                             summary="Autenticación básica",
                             description="Endpoint protegido con autenticación HTTP Basic")
    async def basic_auth(username: str = Depends(verify_basic_auth)):
        """GET /basic-auth - Endpoint con autenticación básica"""
        return AuthResponse(status="authenticated", user=username)
