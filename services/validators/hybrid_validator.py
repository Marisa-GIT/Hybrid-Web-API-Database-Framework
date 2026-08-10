import logging

logger = logging.getLogger(__name__)


class HybridValidator:

    @staticmethod
    def assert_user_flow(api_user, db_user, expected_user_id):
        """
        Validate that each layer successfully returned the expected user.
        """

        # API validation
        assert api_user is not None, "API did not return a user."
        assert api_user["id"] == expected_user_id, (
            f"Expected API user ID {expected_user_id}, "
            f"but got {api_user['id']}."
        )

        # Database validation
        assert db_user is not None, "Database did not return a user."
        assert db_user["id"] == expected_user_id, (
            f"Expected database user ID {expected_user_id}, "
            f"but got {db_user['id']}."
        )

        logger.info(
            "Hybrid validation passed for user ID %s.",
            expected_user_id
        )