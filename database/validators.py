from .schemas import DatabaseSchemas
from core.logger import Logger

logger = Logger.get_logger(__name__)

class DatabaseValidator:

    @staticmethod
    def assert_not_empty_list(data):
        assert data is not None
        assert isinstance(data, list), f"Se esperaba una lista de la BD, pero se obtuvo {type(data).__name__}."
        assert len(data) > 0, "La consulta a la base de datos no devolvió ningún registro (lista vacía)."
        logger.info("Database query returned %d records.", len(data))

    @staticmethod
    def assert_user_exists(user):
        assert user is not None, "El usuario consultado no existe en la base de datos (se obtuvo None)."
        assert isinstance(user, dict), f"Se esperaba un diccionario de usuario, pero se recibió {type(user).__name__}."
        logger.info(f"Validación exitosa: El usuario con ID {user.get('id')} existe en la base de datos.")

    @staticmethod
    def assert_user_schema(user, expected_schema=None):
        DatabaseValidator.assert_user_exists(user)

        schema = expected_schema or DatabaseSchemas.USER_SCHEMA
    
        for field, expected_type in schema.items():
            
            assert field in user, (
                f"Falta la columna/campo '{field}' en el registro de la BD. "
                f"Campos presentes: {set(user.keys())}"
            )

            
            actual_value = user[field]
            
            
            if actual_value is not None:
                assert isinstance(actual_value, expected_type.__name__), (
                    f"Tipo de dato incorrecto en BD para el campo '{field}'. "
                    f"Se esperaba {expected_type.__name__}, pero se obtuvo {type(actual_value).__name__} (Valor: {actual_value})"
                )

        logger.info("Validación exitosa: El esquema del usuario en BD es correcto.")

    @staticmethod
    def assert_user_id(user, expected_id):
        DatabaseValidator.assert_user_exists(user)
        actual_id = user.get("id")

        assert actual_id == expected_id, (
            f"El ID del usuario en BD no coincide. "
            f"Se esperaba ID: {expected_id}, pero se obtuvo ID: {actual_id}."
        )
        logger.info(f"Validación exitosa: El ID del usuario ({actual_id}) coincide con el esperado.")