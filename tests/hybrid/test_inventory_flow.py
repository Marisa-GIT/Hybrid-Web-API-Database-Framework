
from utils.test_data_manager import TestDataManager

class TestInventoryFlow:

    def test_inventory_product_flow(self, hybrid_service):

        user = TestDataManager.get_user("standard_user")
        product = TestDataManager.get_product("backpack")

        inventory_page = hybrid_service.validate_inventory_flow(
            username=user["username"],
            password=user["password"],
            product=product
        )

        assert inventory_page is not None
