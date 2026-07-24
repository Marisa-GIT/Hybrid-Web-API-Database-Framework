from selenium.webdriver.common.by import By
from core.base_page import BasePage
from locators.login_locators import LoginLocators
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):
    
    def is_loaded(self):
        return (
            self.is_visible(LoginLocators.USERNAME)
            and self.is_visible(LoginLocators.PASSWORD)
            and self.is_visible(LoginLocators.LOGIN_BUTTON)
        )

    def login(self, username, password):

        self.logger.info("Logging into the application")

        self.type(LoginLocators.USERNAME, username)
        self.type(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)

        return InventoryPage(self.driver)
    
    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def is_login_button_visible(self):
        return self.is_visible(LoginLocators.LOGIN_BUTTON)

    def is_login_page_loaded(self):
        return self.is_visible(LoginLocators.USERNAME) and self.is_visible(LoginLocators.PASSWORD) and self.is_element_visible(LoginLocators.LOGIN_BUTTON)
    
    