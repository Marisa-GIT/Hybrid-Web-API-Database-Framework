from services.validators.hybrid_validator import HybridValidator
from utils.test_data_manager import TestDataManager


class TestCheckoutFlow:

    def test_purchase_product(self, hybrid_service):

        user = TestDataManager.get_user("standard_user")
        product = TestDataManager.get_product("backpack")

        complete_page = hybrid_service.purchase_product(
            username=user["username"],
            password=user["password"],
            product_name=product["name"],
            first_name="Test",
            last_name="User",
            postal_code="110111"
        )

        assert complete_page.is_loaded()

        assert complete_page.get_complete_header() == "Thank you for your order!"

        assert "Your order has been dispatched" in (
            complete_page.get_complete_message()
        )

    def test_checkout_summary(self, hybrid_service):

        user = TestDataManager.get_user("standard_user")
        product = TestDataManager.get_product("backpack")

        overview_page = hybrid_service.checkout_product(
            username=user["username"],
            password=user["password"],
            product_name=product["name"],
            first_name="Juan",
            last_name="Pérez",
            postal_code="110111"
        )

        assert overview_page.is_loaded()

        products_in_overview = overview_page.get_product_names()

        assert product["name"] in products_in_overview

        HybridValidator.assert_checkout_totals(overview_page)
