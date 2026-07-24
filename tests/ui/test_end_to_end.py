from pages.login_page import LoginPage
from utils.test_data_manager import TestDataManager

class TestCheckout:

    def test_complete_purchase(self, login):
        inventory_page = login()

        product = TestDataManager.get_product("backpack")

        inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()
        assert cart_page.is_loaded()

        checkout_information_page = cart_page.checkout()
        assert checkout_information_page.is_loaded()

        checkout_information_page.complete_information(
            "Ana Maria",
            "Perez",
            "111071"
        )
        checkout_overview_page = checkout_information_page.submit_information()
        assert checkout_overview_page.is_loaded()

        checkout_complete_page = checkout_overview_page.finish()
        assert (
            checkout_complete_page.get_complete_header()
            == "Thank you for your order!"
        )
    
    def test_purchace_multiple_products(self, login):
        inventory_page = login()

        products_to_purchanse = TestDataManager.get_specific_products(["fleece_jacket", "labs_onesie", "bolt_tshirt"]) 
        
        for product in products_to_purchanse:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()
        assert cart_page.is_loaded()

        checkout_information_page = cart_page.checkout()
        assert checkout_information_page.is_loaded()

        checkout_information_page.complete_information(
            "Ana Maria",
            "Perez",
            "111071"
        )

        checkout_overview_page = checkout_information_page.submit_information()
        assert checkout_overview_page.is_loaded()

        checkout_complete_page = checkout_overview_page.finish()
        assert (
            checkout_complete_page.get_complete_header()
            == "Thank you for your order!"
        )

    def test_purchase_two_products(self, login):
        inventory_page = login()

        purchase_two_products = TestDataManager.get_specific_products(
            ["fleece_jacket", "labs_onesie"]
        )

        for product in purchase_two_products:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()

        checkout_info_page.complete_information("Juan", "Pérez", "110111")
        checkout_overview_page = checkout_info_page.submit_information()

        checkout_complete_page = checkout_overview_page.finish()

        success_message = checkout_complete_page.get_complete_header()
        assert success_message == "Thank you for your order!", \
            f"The purchase failed or the message is incorrect. Message obtained: '{success_message}'"

    def test_purchase_after_remove_product(self, login):
        inventory_page = login()

        purchase_two_products = TestDataManager.get_specific_products(
            ["fleece_jacket", "bolt_tshirt"]
        )

        for product in purchase_two_products:
            inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        product = TestDataManager.get_product("fleece_jacket")

        cart_page.remove_product(product["name"])

        checkout_info_page = cart_page.checkout()

        checkout_info_page.complete_information("Juan", "Pérez", "110111")
        checkout_overview_page = checkout_info_page.submit_information()

        checkout_complete_page = checkout_overview_page.finish()

        success_message = checkout_complete_page.get_complete_header()
        assert success_message == "Thank you for your order!", \
            f"The purchase failed or the message is incorrect. Message obtained: '{success_message}'"
        
    def test_purchase_problem_user(self, login):
        inventory_page = login("problem_user")
     
        product = TestDataManager.get_product("bike_light")
        inventory_page.add_product_to_cart(product["name"])

        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()

        checkout_info_page.fill_first_name("John")
        checkout_info_page.fill_last_name("Due")
        checkout_info_page.fill_postal_code("111076")
        checkout_info_page.submit_information()

        assert checkout_info_page.get_error_message() == "Error: Last Name is required"

    def test_purchase_performance_glitch_user(self, login):
            inventory_page = login("perform_glitch_user")
    
            product = TestDataManager.get_product("backpack")
            inventory_page.add_product_to_cart(product["name"])

            cart_page = inventory_page.open_cart()
            checkout_info_page = cart_page.checkout()
            checkout_info_page.complete_information("Juan", "Pérez", "110111")
            checkout_overview_page = checkout_info_page.submit_information()
            checkout_complete_page = checkout_overview_page.finish()

            success_message = checkout_complete_page.get_complete_header()
            assert success_message == "Thank you for your order!", \
                f"The purchase failed or the message is incorrect. Message obtained: '{success_message}'"


    def test_complete_checkout_flow(self, login):
        inventory_page = login()

        products_to_purchase = TestDataManager.get_specific_products(
            [
                "backpack",
                "bike_light",
                "bolt_tshirt"
            ]
        )

        expected_names = []
        for product in products_to_purchase:
            inventory_page.add_product_to_cart(product["name"])
            expected_names.append(product["name"])

        assert inventory_page.get_cart_badge_count() == len(expected_names)

        cart_page = inventory_page.open_cart()
        assert cart_page.get_product_count() == len(expected_names)

        product_names = cart_page.get_product_names()
        for name in expected_names:
            assert name in product_names

        checkout_info_page = cart_page.checkout()
        checkout_overview_page = (
            checkout_info_page
            .complete_information("Juan", "Pérez", "110111")
            .submit_information()
        )

        assert checkout_overview_page.get_product_count() == len(expected_names)

        overview_names = checkout_overview_page.get_product_names()
        for name in expected_names:
            assert name in overview_names

        assert checkout_overview_page.get_item_total() > 0
        assert checkout_overview_page.get_tax() > 0

        expected_total = (
            checkout_overview_page.get_item_total()
            + checkout_overview_page.get_tax()
        )
        assert checkout_overview_page.get_total() == expected_total

        checkout_complete_page = checkout_overview_page.finish()
        assert checkout_complete_page.is_loaded()
        assert checkout_complete_page.get_complete_header() == "Thank you for your order!"
        assert checkout_complete_page.get_complete_message() == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        

