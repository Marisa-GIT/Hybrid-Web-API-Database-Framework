from utils.test_data_manager import TestDataManager


class TestHybridUserFlow:

    def test_hybrid_dependencies(self, hybrid_service):
        """Verify that the HybridService is correctly initialized."""

        assert hybrid_service is not None
        assert hybrid_service.driver is not None
        assert hybrid_service.user_api_client is not None
        assert hybrid_service.user_repository is not None

    def test_user_can_login(self, hybrid_service):

        user = TestDataManager.get_user("standard_user")

        inventory_page = hybrid_service.login_user(
            user["username"],
            user["password"]
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

    def test_validate_user_flow(self, hybrid_service):

        result = hybrid_service.validate_user_flow(1)

        assert result is not None

    def test_login_and_validate_user(self, hybrid_service):

        user = TestDataManager.get_user("standard_user")

        result = hybrid_service.login_and_validate_user(
            username=user["username"],
            password=user["password"],
            user_id=1
        )

        assert result["inventory_page"] is not None
    
    def test_add_product_to_cart(self, hybrid_service):

        product = TestDataManager.get_product("backpack")
        user = TestDataManager.get_user("standard_user")

        cart_page = hybrid_service.add_product_to_cart(
            username=user["username"],
            password=user["password"],
            product_name=product["name"]
        )
        hybrid_service.validate_cart_product(
            cart_page,
            product
        )
