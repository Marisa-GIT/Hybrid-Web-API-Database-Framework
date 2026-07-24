
from typing import TYPE_CHECKING
from core.base_page import BasePage
from locators.checkout_complete_locators import CheckoutCompleteLocators

if TYPE_CHECKING:
    from pages.inventory_page import InventoryPage

class CheckoutCompletePage(BasePage):

    def is_loaded(self) -> bool:
        self.logger.info("Checking if Checkout Complete page is loaded")
        return self.is_visible(CheckoutCompleteLocators.COMPLETE_CONTAINER)
    
    def get_complete_header(self) -> str:
        self.logger.info("Getting complete header text")
        return self.get_text(CheckoutCompleteLocators.COMPLETE_HEADER)
    
    def get_complete_message(self) -> str:
        self.logger.info("Getting complete message text")
        return self.get_text(CheckoutCompleteLocators.COMPLETE_MESSAGE)

    def back_home(self) -> "InventoryPage":
        self.logger.info("Navigating back to home page")
        # Local import to avoid circular dependency
        from pages.inventory_page import InventoryPage
        self.click(CheckoutCompleteLocators.BACK_HOME_BUTTON)
        return InventoryPage(self.driver)