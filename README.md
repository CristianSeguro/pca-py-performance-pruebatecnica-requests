# Mock API Server - Prueba Técnica de requests

## 📋 Descripción del Proyecto

Este proyecto implementa un **Mock API Server** usando **FastAPI** con endpoints organizados modularmente. El objetivo es practicar el uso de la librería `requests` de Python implementando diferentes casos de prueba que cubren aspectos como autenticación, manejo de errores, timeouts, y validación de respuestas.

<div style="border-left: 6px solid red; padding: 10px;">
<strong>
<h1>⚠️ Nota importante:</h1> 
Entre prueba y prueba se recomienda reiniciar el servidor mock para evitar problemas de estado. Puedes hacerlo presionando en la terminal donde se levanto el mock las teclas <code>ctrl + c</code> y luego ejecutando nuevamente el comando <code>python mock_api_server_fastapi.py</code>
<p>Esto es necesario porque el mock no se reinicia automáticamente entre pruebas y puede generar inconsistencias en los datos creados, actualizados o eliminados.
</p>
</strong>
</div>


## 🚀 Configuración e Instalación

### 0. Crear Entorno Virtual (opcional pero recomendado)
```bash
#Creación de un entorno virtual para evitar conflictos de dependencias
python -m venv venv
# Activar el entorno virtual
# En Linux o Mac:
source venv/bin/activate 
# En Windows:
venv\Scripts\activate
```

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar el Mock Server

En una terminal, ejecuta el siguiente comando para iniciar el servidor:

```bash
python mock_api_server_fastapi.py
```

El servidor estará disponible en: **http://localhost:8000**

### 3. Verificar Documentación

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎯 Casos de Prueba a Implementar

Tu tarea es **implementar las funciones en `main.py`** que consuman los endpoints del Mock API Server. Cada función debe retornar valores específicos que serán validados por los tests.

### Proceso de Desarrollo

1. **Analizar el enunciado**: Cada función en `main.py` tiene un enunciado detallado
2. **Implementar la función**: Usar la librería `requests` según las instrucciones
3. **Validar manualmente**: Ejecutar `python main.py`
4. **Validar automáticamente**: Ejecutar `pytest test.py -v`

### Ejemplo de Implementación

#### Antes (esqueleto):
```python
def get_users_list():
    """
    Enunciado: Consultar la lista de usuarios disponibles sin errores, 
    utilizando paginación por defecto.
    
    Entrada: Sin parámetros o ?page=1&limit=10
    Resultado esperado: Código 200 con lista de usuarios en formato JSON
    
    Retorna: (status_code, page, limit, total) desde la respuesta a la petición
    """
    # Tu código aquí
    pass
```

#### Después (implementado):
```python
def get_users_list():
    """
    Enunciado: Consultar la lista de usuarios disponibles sin errores, 
    utilizando paginación por defecto.

    Entrada: Sin parámetros o ?page=1&limit=10
    Resultado esperado: Código 200 con lista de usuarios en formato JSON

    Retorna: (status_code, page, limit, total) desde la respuesta a la petición
    """
    response = requests.get(f"{BASE_URL}/users/")
    data = response.json()
    return (data["status_code"], data["page"], data["limit"], data["total"])
```

## 📋 Lista de Casos de Prueba

### 👥 Usuarios (`/users`)
- [ ] `test_get_users_list()` - Obtener lista de usuarios
- [ ] `test_create_user()` - Crear nuevo usuario
- [ ] `test_get_user_by_id()` - Obtener usuario por ID
- [ ] `test_update_user()` - Actualizar usuario
- [ ] `test_delete_user()` - Eliminar usuario

### 🔐 Autenticación (`/autenticacion`)
- [ ] `test_login_with_form_data()` - Login con form data
- [ ] `test_secure_endpoint_with_headers()` - Headers personalizados
- [ ] `test_bearer_token_auth()` - Bearer Token
- [ ] `test_basic_auth()` - Autenticación básica HTTP


## ▶️ Ejecución

### Ejecutar Casos de Prueba Manuales

```bash
# Ejecutar todos los casos implementados
python main.py
```

**Salida esperada:**
```
🚀 Ejecutando Casos de Prueba del Mock API Server
============================================================
✅ Servidor Mock API conectado correctamente
📡 Versión: 1.0.0

🧪 Ejecutando  1/14: test_get_users_list
✅ test_get_users_list - Completado

🧪 Ejecutando  2/14: test_create_user
⚠️  test_create_user - Pendiente de implementar
...
```

### Ejecutar Tests Automatizados

```bash
# Ejecutar todos los tests
pytest test.py -v

# Ejecutar con coverage
pytest test.py -v --cov=main

# Ejecutar un test específico
pytest test.py::TestMockAPIServer::test_get_users_list_implementation -v

# Ejecutar tests por categoría
pytest test.py -k "user" -v                    # Solo tests de usuarios
pytest test.py -k "auth" -v                    # Solo tests de autenticación
pytest test.py -k "test_slow" -v               # Solo test lento
```

**Salida esperada:**
```
========================= test session starts =========================
test.py::TestMockAPIServer::test_get_users_list_implementation PASSED
test.py::TestMockAPIServer::test_create_user_implementation PASSED
test.py::TestMockAPIServer::test_get_user_by_id_implementation PASSED
...
========================= 14 passed in 10.45s =========================
```

## 🔧 Credenciales de Prueba

### Usuarios Válidos
```
Username: admin    | Password: password
Username: user     | Password: 123456
```

### Tokens Bearer Válidos
```
abc123token
token456  
secrettoken
```

### Datos de Usuarios Existentes
```json
[
  {"id": 1, "name": "Juan Pérez", "email": "juan@example.com"},
  {"id": 2, "name": "María García", "email": "maria@example.com"},
  {"id": 3, "name": "Carlos López", "email": "carlos@example.com"}
]
```
## 🐛 Troubleshooting

### Error: Connection Refused
```
❌ Error: No se puede conectar al Mock API Server
```
**Solución**: Ejecutar el servidor mock en otra terminal:
```bash
python mock_api_server_fastapi.py
```

### Error: Module Not Found
```
ModuleNotFoundError: No module named 'requests'
```
**Solución**: Instalar dependencias:
```bash
pip install requests pytest
```

### Error: Tests Fallan
```
AssertionError: assert 404 == 200
```
**Solución**: Verificar que:
1. El servidor mock esté ejecutándose
2. Los endpoints sean correctos
3. Los datos de entrada sean válidos

### Error: Puerto en Uso
```
OSError: [Errno 48] Address already in use
```
**Solución**: 
```bash
# Cambiar puerto en mock_api_server_fastapi.py
uvicorn.run(..., port=8001)

# O matar procesos existentes
pkill -f python  # Linux/macOS
taskkill /F /IM python.exe  # Windows
```

## 📈 Métricas de Éxito

### Implementación Completa
- ✅ 14/14 funciones implementadas
- ✅ Todos los tests pasan
- ✅ Coverage > 80%

### Criterios de Validación
1. **Funcionalidad**: Cada caso debe cumplir su enunciado
2. **Manejo de errores**: Responses incorrectos deben manejarse
3. **Validación de datos**: Verificar estructura de respuestas
4. **Códigos HTTP**: Validar status codes correctos
5. **Headers**: Verificar headers cuando sea necesario

## 🎯 Objetivos de Aprendizaje

Después de completar este ejercicio, habrás aprendido:

- ✅ **Requests básicos**: GET, POST, PUT, DELETE
- ✅ **Autenticación HTTP**: Basic, Bearer Token, Form Data
- ✅ **Manejo de Headers**: Personalizados y de autenticación
- ✅ **Validación de respuestas**: Status codes, JSON, estructura
- ✅ **Testing con pytest**: Assertions, fixtures, parametrización
- ✅ **APIs REST**: Patrones y mejores prácticas
- ✅ **Debugging**: Identificación y resolución de errores

## 📚 Recursos Adicionales

- [Documentación de Requests](https://docs.python-requests.org/)
- [Documentación de Pytest](https://docs.pytest.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [REST API Best Practices](https://restfulapi.net/)

---

**¡Buena suerte con la implementación! 🚀**

Si encuentras algún problema, revisa la documentación del Mock API en http://localhost:8000/docs

## Control de Versiones

|autor|fecha|cambios|
|---|---|---|
|Cristian Seguro|2025-08-06|Creación del proyecto|
