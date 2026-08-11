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
