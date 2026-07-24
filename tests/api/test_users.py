import pytest
from api.response_validator import ResponseValidator


class TestUsersAPI:

    def test_get_all_users(self, user_api_client):
        """Escenario: Obtener todos los usuarios"""
        response = user_api_client.get_all_users()
        
        ResponseValidator.assert_status_code(response, 200)
        
        users_data = response.json()
        ResponseValidator.validate_not_empty_list(users_data)
        ResponseValidator.assert_user_schema(users_data[0])

    def test_get_user_by_id(self, user_api_client):
        """Escenario: Obtener un usuario por ID válido"""
        user_id = 1
        response = user_api_client.get_user_by_id(user_id)
        
        ResponseValidator.assert_status_code(response, 200)
        
        user_data = response.json()
        ResponseValidator.assert_user_id(user_data, user_id)
        ResponseValidator.assert_user_schema(user_data)

    @pytest.mark.parametrize("invalid_id", [9999, -1, 0])
    def test_get_user_not_found(self, user_api_client, invalid_id):
        """Escenario: Validar respuesta al buscar usuarios con IDs inválidos"""
        response = user_api_client.get_user_by_id(invalid_id)
        ResponseValidator.assert_status_code(response, 404)