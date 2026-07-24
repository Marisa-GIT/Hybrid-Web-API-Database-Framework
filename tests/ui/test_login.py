import pytest
from pages.inventory_page import InventoryPage
from utils.test_data_manager import TestDataManager
from pages.login_page import LoginPage
class TestLogin:

    def test_successful_login(self, login):
        inventory_page = login()

        assert inventory_page.is_loaded()
    
    def test_locked_login(self, driver):
        login_page = LoginPage(driver)

        user = TestDataManager.get_user("locked_user")

        login_page.login(user["username"], user["password"])

        assert login_page.get_error_message() == \
            "Epic sadface: Sorry, this user has been locked out."

@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce")
    ]
)

def test_login_multiple_users(
    driver,
    username,
    password
):
   
    login = LoginPage(driver)
    login.login(username, password)
    
    inventory = InventoryPage(driver)
    assert inventory.get_page_title() == "Products"