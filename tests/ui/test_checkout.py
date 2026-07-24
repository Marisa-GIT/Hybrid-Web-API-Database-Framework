from utils.test_data_manager import TestDataManager

class TestCheckout:

    def test_checkout_first_name_required(self, login):                   
        inventory_page = login()
        
        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()
        checkout_info_page.submit_information()

        assert checkout_info_page.get_error_message() == "Error: First Name is required"

    def test_checkout_last_name_required(self, login):
        inventory_page = login()
        
        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()
        checkout_info_page.fill_first_name("John")
        checkout_info_page.submit_information()

        assert checkout_info_page.get_error_message() == "Error: Last Name is required"

    def test_checkout_postal_code_required(self, login):
        inventory_page = login()
        
        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()
        checkout_info_page.fill_first_name("John")
        checkout_info_page.fill_last_name("Doe")
        checkout_info_page.submit_information()

        assert checkout_info_page.get_error_message() == "Error: Postal Code is required"

    def test_cancel_checkout(self, driver, login):
        inventory_page = login()
        
        cart_page = inventory_page.open_cart()

        checkout_info_page = cart_page.checkout()

        checkout_info_page = checkout_info_page.cancel()

        assert "cart.html" in driver.current_url, "It was not returned to the cart upon cancelation."

    def test_checkout_summary_and_completion(self, login):
            inventory_page = login()
         

            products_to_purchanse = TestDataManager.get_specific_products(["backpack", "bike_light"]) 
        
            for product in products_to_purchanse:
                inventory_page.add_product_to_cart(product["name"])

            cart_page = inventory_page.open_cart()

            checkout_info_page = cart_page.checkout()
            checkout_info_page.complete_information("Juan", "Pérez", "110111")

            overview_page = checkout_info_page.submit_information()

            products_in_overview = overview_page.get_product_names()
            assert "Sauce Labs Backpack" in products_in_overview
            assert "Sauce Labs Bike Light" in products_in_overview

            product_prices = overview_page.get_product_prices()
            subtotal = overview_page.get_item_total() 
            tax = overview_page.get_tax()              
            total = overview_page.get_total()  

            expected_subtotal = round(sum(product_prices), 2)
            assert subtotal == expected_subtotal, \
                f"The subtotal of the UI ({subtotal}) does not match the sum of its products. ({expected_subtotal})"

            expected_tax = round(subtotal * 0.08, 2)
            assert tax == expected_tax, \
                f"The tax calculated by the system ({tax}) is not the expected 8%. ({expected_tax})"

            expected_total = round(subtotal + tax, 2)
            assert total == expected_total, \
                f"The final total of the UI ({total}) does not equal the sum of subtotal + tax. ({expected_total})"
            
            complete_page = overview_page.finish()
            assert complete_page.get_complete_header() == "Thank you for your order!", \
                "The final success message of the purchase was not displayed."
