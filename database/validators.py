from .schemas import DatabaseSchemas
from core.logger import Logger

logger = Logger.get_logger(__name__)

class DatabaseValidator:

    @staticmethod
    def assert_not_empty_list(data):
        """Validates that the database query result is not None and is a non-empty list."""
        assert data is not None, "Database query returned None."
        assert isinstance(data, list), (
            f"Expected a list from database, but got {type(data).__name__}."
        )
        assert len(data) > 0, (
            "Database query returned no records (empty list)."
        )

        logger.info("Database query returned %d records.", len(data))

    @staticmethod
    def assert_user_exists(user):
        """Validates that the fetched user object exists and is a dictionary."""
        assert user is not None, (
            "The requested user does not exist in the database."
        )

        assert isinstance(user, dict), (
            f"Expected a dictionary, but got {type(user).__name__}."
        )

        logger.info(
            "User with ID %s exists.",
            user.get("id")
        )

    @staticmethod
    def assert_user_schema(user, expected_schema=None):
        """Validates that the user record contains the required fields and matching data types."""
        DatabaseValidator.assert_user_exists(user)

        schema = expected_schema or DatabaseSchemas.USER_SCHEMA

        for field, expected_type in schema.items():
            # 1. Validate field existence
            assert field in user, (
                f"Missing field/column '{field}' in database record. "
                f"Present fields: {set(user.keys())}"
            )

            actual_value = user[field]

            # 2. Validate data type if value is not NULL
            if actual_value is not None:
                assert isinstance(actual_value, expected_type), (
                    f"Incorrect data type for field '{field}'. "
                    f"Expected {expected_type.__name__}, "
                    f"but got {type(actual_value).__name__}."
                )

        logger.info("User schema validation passed.")

    @staticmethod
    def assert_user_id(user, expected_id):
        """Validates that the user ID in the database record matches the expected ID."""
        DatabaseValidator.assert_user_exists(user)
        actual_id = user.get("id")

        assert actual_id == expected_id, (
            f"User ID mismatch in database. "
            f"Expected ID: {expected_id}, but got ID: {actual_id}."
        )
        logger.info("User ID validation passed.")