"""
Tests de Validación - Mock API Server
====================================

Archivo de tests con pytest para validar que las funciones implementadas
en main.py retornen los valores correctos según los casos de prueba.

Para ejecutar:
1. Instalar pytest: pip install pytest
2. Asegurar que el Mock API Server esté ejecutándose
3. Implementar las funciones en main.py
4. Ejecutar tests: pytest test.py -v
"""

import pytest
import requests
from main import *
# from ejemplo_solucion import *


class TestMockAPIServerFunctions:
    """Clase de tests para validar las funciones implementadas en main.py"""
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup que se ejecuta antes de cada test"""
        # Verificar que el servidor esté disponible
        try:
            response = requests.get(f"{BASE_URL}/")
            assert response.status_code == 200
        except requests.exceptions.ConnectionError:
            pytest.skip("Mock API Server no está disponible en http://localhost:8000")
    
    # =========================================================================
    # 🧑‍💼 TESTS - USUARIOS
    # =========================================================================
    
    def test_get_users_list_returns_correct_values(self):
        """Test que valida que get_users_list() retorne los valores correctos"""
        result = get_users_list()
        
        # Verificar que la función no retorne None (está implementada)
        assert result is not None, "La función get_users_list() debe estar implementada y retornar valores"
        
        # Verificar que retorne una tupla de 4 elementos
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 4, "Debe retornar exactamente 4 valores: (status_code, page, limit, total)"
        
        status_code, page, limit, total = result
        
        # Verificar tipos y valores esperados
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(page, int), "page debe ser un entero"
        assert isinstance(limit, int), "limit debe ser un entero"
        assert isinstance(total, int), "total debe ser un entero"
        
        # Verificar valores específicos esperados
        assert status_code == 200, "El status_code debe ser 200"
        assert page == 1, "La página por defecto debe ser 1"
        assert limit == 10, "El límite por defecto debe ser 10"
        assert total >= 0, "El total debe ser mayor o igual a 0"
    
    def test_create_user_returns_correct_values(self):
        """Test que valida que create_user() retorne los valores correctos"""
        result = create_user()
        
        assert result is not None, "La función create_user() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 4, "Debe retornar exactamente 4 valores: (status_code, id, name, email)"
        
        status_code, user_id, name, email = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(user_id, int), "id debe ser un entero"
        assert isinstance(name, str), "name debe ser un string"
        assert isinstance(email, str), "email debe ser un string"
        
        assert status_code == 201, "El status_code debe ser 201 para creación exitosa"
        assert user_id > 0, "El ID del usuario debe ser mayor a 0"
        assert len(name) > 0, "El nombre no debe estar vacío"
        assert "@" in email, "El email debe tener formato válido (contener @)"
    
    def test_get_user_by_id_returns_correct_values(self):
        """Test que valida que get_user_by_id() retorne los valores correctos"""
        result = get_user_by_id()
        
        assert result is not None, "La función get_user_by_id() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 4, "Debe retornar exactamente 4 valores: (status_code, id, name, email)"
        
        status_code, user_id, name, email = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(user_id, int), "id debe ser un entero"
        assert isinstance(name, str), "name debe ser un string"
        assert isinstance(email, str), "email debe ser un string"
        
        assert status_code == 200, "El status_code debe ser 200"
        assert user_id == 1, "Debe retornar el usuario con ID 1"
        assert len(name) > 0, "El nombre no debe estar vacío"
        assert "@" in email, "El email debe tener formato válido"
    
    def test_update_user_returns_correct_values(self):
        """Test que valida que update_user() retorne los valores correctos"""
        result = update_user()
        
        assert result is not None, "La función update_user() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 4, "Debe retornar exactamente 4 valores: (status_code, id, name, email)"
        
        status_code, user_id, name, email = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(user_id, int), "id debe ser un entero"
        assert isinstance(name, str), "name debe ser un string"
        assert isinstance(email, str), "email debe ser un string"
        
        assert status_code == 200, "El status_code debe ser 200"
        assert user_id == 1, "Debe retornar el usuario con ID 1"
        assert "Actualizada" in name or "actualizada" in name, "El nombre debe mostrar que fue actualizado"
        assert "actualizada" in email, "El email debe mostrar que fue actualizado"
    
    def test_delete_user_returns_correct_values(self):
        """Test que valida que delete_user() retorne los valores correctos"""
        result = delete_user()
        
        assert result is not None, "La función delete_user() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 2, "Debe retornar exactamente 2 valores: (status_code, response_text)"
        
        status_code, response_text = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(response_text, str), "response_text debe ser un string"
        
        assert status_code == 204, "El status_code debe ser 204 para eliminación exitosa"
        assert response_text == "", "El response_text debe estar vacío para código 204"
    
    # =========================================================================
    # 🔐 TESTS - AUTENTICACIÓN
    # =========================================================================
    
    def test_login_with_form_data_returns_correct_values(self):
        """Test que valida que login_with_form_data() retorne los valores correctos"""
        result = login_with_form_data()
        
        assert result is not None, "La función login_with_form_data() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 4, "Debe retornar exactamente 4 valores: (status_code, success, message, token)"
        
        status_code, success, message, token = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(success, bool), "success debe ser un booleano"
        assert isinstance(message, str), "message debe ser un string"
        assert isinstance(token, str), "token debe ser un string"
        
        assert status_code == 200, "El status_code debe ser 200"
        assert success is True, "success debe ser True para login exitoso"
        assert len(message) > 0, "El mensaje no debe estar vacío"
        assert len(token) > 0, "El token no debe estar vacío"
    
    def test_secure_endpoint_with_headers_returns_correct_values(self):
        """Test que valida que secure_endpoint_with_headers() retorne los valores correctos"""
        result = secure_endpoint_with_headers()
        
        assert result is not None, "La función secure_endpoint_with_headers() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 3, "Debe retornar exactamente 3 valores: (status_code, data, headers_received)"
        
        status_code, data, headers_received = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(data, str), "data debe ser un string"
        assert isinstance(headers_received, dict), "headers_received debe ser un diccionario"
        
        assert status_code == 200, "El status_code debe ser 200"
        assert data == "secured", "data debe ser 'secured'"
        
        # Verificar que los headers específicos estén presentes
        expected_headers = ["User-Agent", "Accept", "X-Custom-Header"]
        for header in expected_headers:
            assert header in headers_received, f"El header '{header}' debe estar presente en la respuesta"
    
    def test_bearer_token_auth_returns_correct_values(self):
        """Test que valida que bearer_token_auth() retorne los valores correctos"""
        result = bearer_token_auth()
        
        assert result is not None, "La función bearer_token_auth() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 3, "Debe retornar exactamente 3 valores: (status_code, user, token)"
        
        status_code, user, token = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(user, str), "user debe ser un string"
        assert isinstance(token, str), "token debe ser un string"
        
        assert status_code == 200, "El status_code debe ser 200"
        assert user == "authenticated", "user debe ser 'authenticated'"
        assert len(token) > 0, "El token no debe estar vacío"
    
    def test_basic_auth_returns_correct_values(self):
        """Test que valida que basic_auth() retorne los valores correctos"""
        result = basic_auth()
        
        assert result is not None, "La función basic_auth() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 3, "Debe retornar exactamente 3 valores: (status_code, status, user)"
        
        status_code, status, user = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(status, str), "status debe ser un string"
        assert isinstance(user, str), "user debe ser un string"
        
        assert status_code == 200, "El status_code debe ser 200"
        assert status == "authenticated", "status debe ser 'authenticated'"
        assert user in ["admin", "user"], "user debe ser uno de los usuarios válidos"
    
    # =========================================================================
    # 🧪 TESTS - TESTING
    # =========================================================================
    
    def test_slow_endpoint_returns_correct_values(self):
        """Test que valida que slow_endpoint() retorne los valores correctos"""
        result = slow_endpoint()
        
        assert result is not None, "La función slow_endpoint() debe estar implementada"
        assert isinstance(result, tuple), "Debe retornar una tupla"
        assert len(result) == 4, "Debe retornar exactamente 4 valores: (status_code, data, delay, elapsed_time)"
        
        status_code, data, delay, elapsed_time = result
        
        assert isinstance(status_code, int), "status_code debe ser un entero"
        assert isinstance(data, str), "data debe ser un string"
        assert isinstance(delay, int), "delay debe ser un entero"
        assert isinstance(elapsed_time, (int, float)), "elapsed_time debe ser un número"
        
        assert status_code == 200, "El status_code debe ser 200"
        assert data == "slow response", "data debe ser 'slow response'"
        assert delay == 3, "delay debe ser 3 segundos"
        assert elapsed_time >= 2.5, "El tiempo transcurrido debe ser al menos 2.5 segundos"
        assert elapsed_time <= 5.0, "El tiempo transcurrido no debe exceder 5 segundos"
    
    

class TestImplementationStatus:
    """Tests para verificar el estado de implementación de las funciones"""
    
    def test_all_functions_implemented(self):
        """Test que verifica que todas las funciones estén implementadas (no retornen None)"""
        functions_to_test = [
            ("get_users_list", get_users_list),
            ("create_user", create_user),
            ("get_user_by_id", get_user_by_id),
            ("update_user", update_user),
            ("delete_user", delete_user),
            ("login_with_form_data", login_with_form_data),
            ("secure_endpoint_with_headers", secure_endpoint_with_headers),
            ("bearer_token_auth", bearer_token_auth),
            ("basic_auth", basic_auth),
            ("slow_endpoint", slow_endpoint)
        ]
        
        # Verificar disponibilidad del servidor
        try:
            requests.get(f"{BASE_URL}/", timeout=5)
        except requests.exceptions.ConnectionError:
            pytest.skip("Mock API Server no está disponible")
        
        unimplemented_functions = []
        
        for func_name, func in functions_to_test:
            try:
                result = func()
                if result is None:
                    unimplemented_functions.append(func_name)
            except Exception:
                # Si hay una excepción, consideramos que está implementada pero con errores
                pass
        
        if unimplemented_functions:
            pytest.fail(
                f"Las siguientes funciones no están implementadas (retornan None): "
                f"{', '.join(unimplemented_functions)}"
            )


# Configuración adicional de pytest
def pytest_configure(config):
    """Configuración global de pytest"""
    config.addinivalue_line(
        "markers", "slow: marca tests que tardan más tiempo en ejecutarse"
    )


@pytest.fixture(scope="session")
def mock_server_check():
    """Fixture que verifica la disponibilidad del servidor antes de ejecutar tests"""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code != 200:
            pytest.exit("Mock API Server no responde correctamente")
    except requests.exceptions.ConnectionError:
        pytest.exit("Mock API Server no está disponible. Ejecuta: python mock_api_server_fastapi.py")
    except requests.exceptions.Timeout:
        pytest.exit("Mock API Server no responde en tiempo esperado")


# Marcar todos los tests para usar el fixture de verificación de servidor
pytestmark = pytest.mark.usefixtures("mock_server_check")

