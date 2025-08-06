"""
Mock API Server
=================================

Este archivo contiene las funciones que implementan el consumo de la API
usando la librería requests. Cada función debe implementar el enunciado
y retornar los valores específicos solicitados.

Para ejecutar:
1. Asegúrate de que el Mock API Server esté ejecutándose en http://localhost:8000
2. Implementa cada función siguiendo el enunciado
3. Ejecuta este archivo: python main.py
4. Valida con pytest: pytest test.py
"""

import requests
import base64
import time
from typing import Dict, Any, Optional, Tuple


# =============================================================================
# CONFIGURACIÓN BASE
# =============================================================================

BASE_URL = "http://localhost:8000"

# Credenciales de prueba (según configuración del mock)
VALID_CREDENTIALS = {
    "admin": "password",
    "user": "123456"
}

VALID_TOKENS = ["abc123token", "token456", "secrettoken"]


# =============================================================================
# 🧑‍💼 CASOS DE PRUEBA - USUARIOS
# =============================================================================

def get_users_list() -> Tuple[int, int, int, int]:
    """
    Enunciado: Consultar la lista de usuarios disponibles sin errores, 
    utilizando paginación por defecto.
    
    Entrada: Sin parámetros o ?page=1&limit=10
    Resultado esperado: Código 200 con lista de usuarios en formato JSON
    
    Retorna: (status_code, page, limit, total) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


def create_user() -> Tuple[int, int, str, str]:
    """
    Enunciado: Crear un nuevo usuario válido proporcionando nombre y correo electrónico.
    
    Entrada: JSON con name y email
    Resultado esperado: Código 201 con datos del usuario creado
    
    Retorna: (status_code, id, name, email) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


def get_user_by_id() -> Tuple[int, int, str, str]:
    """
    Enunciado: Obtener los datos de un usuario existente mediante su ID.
    
    Entrada: user_id = 1
    Resultado esperado: Código 200 con datos del usuario correspondiente
    
    Retorna: (status_code, id, name, email) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


def update_user() -> Tuple[int, int, str, str]:
    """
    Enunciado: Actualizar los datos (nombre y/o email) de un usuario existente.
    
    Entrada: user_id = 1, JSON con name y email actualizados
    Resultado esperado: Código 200 con los datos del usuario actualizados
    
    Retorna: (status_code, id, name, email) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


def delete_user() -> Tuple[int, str]:
    """
    Enunciado: Eliminar un usuario existente por su ID.
    
    Entrada: user_id = 1
    Resultado esperado: Código 204 (sin contenido)
    
    Retorna: (status_code, response_text) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


# =============================================================================
# 🔐 CASOS DE PRUEBA - AUTENTICACIÓN
# =============================================================================

def login_with_form_data() -> Tuple[int, bool, str, str]:
    """
    Enunciado: Iniciar sesión con credenciales válidas usando application/x-www-form-urlencoded.
    
    Entrada: username=admin&password=password
    Resultado esperado: Código 200 con token de autenticación y mensaje de éxito
    
    Retorna: (status_code, success, message, token) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


def secure_endpoint_with_headers() -> Tuple[int, str, Dict[str, str]]:
    """
    Enunciado: Acceder al endpoint que refleja los headers personalizados enviados.
    
    Entrada: Headers personalizados (User-Agent, Accept, X-Custom-Header)
    Resultado esperado: Código 200 con los headers reflejados en el cuerpo de respuesta
    
    Retorna: (status_code, data, headers_received) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


def bearer_token_auth() -> Tuple[int, str, str]:
    """
    Enunciado: Acceder a un recurso protegido usando un Bearer Token válido.
    
    Entrada: Authorization: Bearer <token_válido>
    Resultado esperado: Código 200 con los datos del usuario autenticado
    
    Retorna: (status_code, user, token) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


def basic_auth() -> Tuple[int, str, str]:
    """
    Enunciado: Acceder a un recurso protegido con autenticación básica HTTP válida.
    
    Entrada: Authorization: Basic <base64(usuario:clave)>
    Resultado esperado: Código 200 con datos del usuario autenticado
    
    Retorna: (status_code, status, user) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


# =============================================================================
# 🧪 CASOS DE PRUEBA - TESTING
# =============================================================================

def slow_endpoint() -> Tuple[int, str, int, float]:
    """
    Enunciado: Probar la respuesta del sistema con una demora controlada.
    
    Entrada: ?delay=3
    Resultado esperado: Código 200 con una respuesta simuladamente lenta (demora de 3 segundos)
    
    Retorna: (status_code, data, delay, elapsed_time) desde la respuesta a la petición
    """
    # Tu código aquí
    pass


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def main():
    """
    Función principal que ejecuta todas las funciones de consumo de API.
    
    Nota: Antes de ejecutar, asegúrate de que el Mock API Server
    esté ejecutándose en http://localhost:8000
    """
    print("🚀 Ejecutando Funciones de Consumo del Mock API Server")
    print("=" * 60)
    
    # Lista de funciones a ejecutar
    api_functions = [
        # Usuarios
        ("Usuarios", [
            get_users_list,
            create_user,
            get_user_by_id,
            update_user,
            delete_user,
        ]),
        
        # Autenticación
        ("Autenticación", [
            login_with_form_data,
            secure_endpoint_with_headers,
            bearer_token_auth,
            basic_auth,
        ]),
        
        # Testing
        ("Testing", [
            slow_endpoint
        ])
    ]
    
    # Verificar conectividad con el servidor
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Servidor Mock API conectado correctamente")
        print(f"📡 Versión: {response.json().get('version', 'N/A')}")
        print()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar al Mock API Server")
        print("💡 Asegúrate de que esté ejecutándose en http://localhost:8000")
        print("🔧 Ejecuta: python mock_api_server_fastapi.py")
        return
    
    # Ejecutar cada función por categoría
    total_functions = sum(len(funcs) for _, funcs in api_functions)
    function_count = 0
    
    for category, functions in api_functions:
        print(f"📂 Categoría: {category}")
        print("-" * 40)
        
        for func in functions:
            function_count += 1
            print(f"🔧 Ejecutando {function_count:2d}/{total_functions}: {func.__name__}()")
            
            try:
                result = func()
                if result is not None:
                    print(f"✅ {func.__name__} - Retornó: {result}")
                else:
                    print(f"⚠️  {func.__name__} - Pendiente de implementar (retornó None)")
            except Exception as e:
                print(f"❌ {func.__name__} - Error: {str(e)}")
            
            print()
        
        print()
    
    print("🎉 Ejecución de funciones completada!")
    print("💡 Para validación automática, ejecuta: pytest test.py -v")


if __name__ == "__main__":
    main()
