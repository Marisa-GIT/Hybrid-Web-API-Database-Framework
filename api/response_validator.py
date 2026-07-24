from api.response_validator import UserSchemas

class UserSchemas:
    USER_SCHEMA_KEYS = {
        "id": int, "name": str , "username": str, "email": str, 
        "address": str, "phone": str, "website": str, "company":str
    }

class ResponseValidator:

    @staticmethod
    def assert_status_code(response, expected_code=200):
        """Valida el código de estado HTTP de la respuesta."""
        assert response.status_code == expected_code, (
            f"Se esperaba status code {expected_code}, pero se obtuvo {response.status_code}"
        )

    @staticmethod
    def assert_not_empty_list(data):
        """Valida que el objeto sea una lista y no esté vacío."""
        assert isinstance(data, list), (
            f"Se esperaba una lista, pero se obtuvo {type(data).__name__}"
        )
        assert len(data) > 0, "La lista recibida está vacía"

    @staticmethod
    def assert_user_schema(user_data):
        """Valida que un objeto de usuario contenga todas las claves requeridas."""
        assert isinstance(user_data, dict), "El objeto de usuario debe ser un diccionario"
        for field, expected_type in UserSchemas.USER_SCHEMA_KEYS.items():
            assert field in user_data
            assert isinstance(user_data[field], expected_type), (
                f"La estructura del usuario no coincide. Claves presentes: {set(user_data.keys())}"
            )

    @staticmethod
    def assert_user_id(user_data, expected_id):
        """Valida que el ID del usuario coincida con el esperado."""
        assert user_data.get("id") == expected_id, (
            f"Se esperaba el ID {expected_id}, pero se obtuvo {user_data.get('id')}"
        )