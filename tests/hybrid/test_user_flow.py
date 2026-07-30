import pytest


class TestHybridUserFlow:

    def test_hybrid_dependencies(self, hybrid_service):
        """Verify that the HybridService is correctly initialized."""

        assert hybrid_service is not None
        assert hybrid_service.driver is not None
        assert hybrid_service.user_api_client is not None
        assert hybrid_service.user_repository is not None

    def test_user_can_login(self, hybrid_service):

        inventory_page = hybrid_service.login_user(
            "standard_user",
            "secret_sauce"
        )

        assert inventory_page is not None

    def test_get_user_from_api(self, hybrid_service):
        user = hybrid_service.get_api_user(1)

        assert user["id"] == 1

    def test_can_retrieve_user_from_api_and_database(self, hybrid_service):
        """Verify that the same user can be retrieved from API and Database."""

        api_user = hybrid_service.get_api_user(1)
        db_user = hybrid_service.get_database_user(1)

        assert api_user is not None
        assert db_user is not None

    def test_user_data_is_consistent_between_api_and_database(self,hybrid_service):
        """Verify that API and Database return consistent user information."""

        api_user, db_user = hybrid_service.validate_user_consistency(1)

        assert api_user["id"] == db_user["id"]
        assert api_user["username"] == db_user["username"]
        assert api_user["email"] == db_user["email"]