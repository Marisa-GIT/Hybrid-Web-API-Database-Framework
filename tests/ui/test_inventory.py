from utils.test_data_manager import TestDataManager


class TestInventory:

    def test_product_catalog_display(self, login):
        inventory_page = login()

        product_names = inventory_page.get_all_product_names()

        backpack = TestDataManager.get_product("backpack")
        bike_light = TestDataManager.get_product("bike_light")

        assert len(product_names) > 0, \
            "The product catalog is empty."

        assert backpack["name"] in product_names, \
            f"{backpack['name']} does not appear in the catalog"

        assert bike_light["name"] in product_names, \
            f"{bike_light['name']} does not appear in the catalog"

    def test_product_sorting_by_price(self, login):
        inventory_page = login()

        inventory_page.select_sort_option("lohi")

        actual_prices = inventory_page.get_all_product_prices()
        expected_prices = sorted(actual_prices)

        assert actual_prices == expected_prices, (
            f"The order failed.\n"
            f"Actual:   {actual_prices}\n"
            f"expected: {expected_prices}"
        )

    def test_add_product_to_cart(self, login):
        inventory_page = login()

        product = TestDataManager.get_product("backpack")

        inventory_page.add_product_to_cart(product["name"])

        assert inventory_page.get_cart_badge_count() == 1, (
            "The cart counter should show 1 product."
        )

    def test_add_multiple_products_to_cart(self, login):
        inventory_page = login()

        products_to_purchase = TestDataManager.get_specific_products(
            [
                "backpack",
                "bike_light",
                "labs_onesie"
            ]
        )

        for product in products_to_purchase:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        products_in_cart = cart_page.get_product_names()

        for product in products_to_purchase:
            assert product["name"] in products_in_cart, (
                f"{product['name']} not found in the cart."
            )

    def test_add_products_updates_cart_badge(self, login):
        inventory_page = login()
        
        assert inventory_page.get_cart_badge_count() == 0, (
            "The cart should start empty."
        )

        backpack = TestDataManager.get_product("backpack")
        bike_light = TestDataManager.get_product("bike_light")

        inventory_page.add_product_to_cart(backpack["name"])

        assert inventory_page.get_cart_badge_count() == 1, (
            "The cart counter should be 1."
        )

        inventory_page.add_product_to_cart(bike_light["name"])

        assert inventory_page.get_cart_badge_count() == 2, (
            "The cart counter should be 2."
        )