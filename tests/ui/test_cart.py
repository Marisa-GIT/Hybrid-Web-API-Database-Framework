from utils.test_data_manager import TestDataManager

class TestCart:

    def test_cart_badge_increments_after_adding_product(self, login):
        inventory_page = login()

        product = TestDataManager.get_product("backpack")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 1

        product = TestDataManager.get_product("bike_light")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 2

    def test_cart_badge_decrements_after_removing_product(self, login):
        inventory_page = login()

        product = TestDataManager.get_product("backpack")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 1

        product = TestDataManager.get_product("bike_light")
        inventory_page.add_product_to_cart(product["name"])
        assert inventory_page.get_cart_badge_count() == 2

        inventory_page.remove_product(product["name"])
        assert inventory_page.get_cart_badge_count() == 1

    def test_continue_shopping_from_cart(self, login):
        inventory_page = login()

        cart_page = inventory_page.open_cart()

        returned_inventory_page = cart_page.continue_shopping()
        assert returned_inventory_page.is_loaded()

    def test_checkout_navigation_from_cart(self, login):
        inventory_page = login()
    
        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()
        assert checkout_info_page.is_loaded()

    





        
            
