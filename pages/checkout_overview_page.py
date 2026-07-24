from typing import TYPE_CHECKING
from core.base_page import BasePage
from locators.checkout_overview_locators import CheckoutOverviewLocators
from pages.checkout_complete_page import CheckoutCompletePage
from selenium.webdriver.support import expected_conditions as EC

if TYPE_CHECKING:
    from pages.inventory_page import InventoryPage

class CheckoutOverviewPage(BasePage):

    def is_loaded(self) -> bool:
        self.logger.info("Checking if Checkout Overview page is loaded")
        return self.is_visible(CheckoutOverviewLocators.OVERVIEW_CONTAINER)
    
    def get_product_names(self) -> list[str]:
        self.logger.info("Getting product names in the checkout overview")
        product_elements = CheckoutOverviewLocators.PRODUCT_NAMES
        return self.get_text_from_elements(product_elements)

    def get_product_prices(self) -> list[float]:
        self.logger.info("Getting product names in the checkout overview")
        price_elements = self.get_elements(CheckoutOverviewLocators.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in price_elements]
        
    def get_item_total(self) -> float:
        self.logger.info("Checking the subtotal on the screen")
        raw_text = self.get_text(CheckoutOverviewLocators.ITEM_TOTAL)
        return float(raw_text.split("$")[1])

    def get_tax(self) -> float:
        self.logger.info("Getting tax from checkout overview")
        text_element = self.get_text(CheckoutOverviewLocators.TAX)
        return float(text_element.split("$")[1])

    def get_total(self) -> float:
        self.logger.info("Getting total from checkout overview")
        text_element = self.get_text(CheckoutOverviewLocators.TOTAL)
        return float(text_element.split("$")[1])
    
    def get_product_count(self) -> int:
        self.logger.info("Getting number of products from inventory")
        return self.get_element_count(
            CheckoutOverviewLocators.PRODUCT_NAMES
        )
    
    def finish(self) -> "CheckoutCompletePage":
        self.logger.info("Finishing checkout")
        self.click(CheckoutOverviewLocators.FINISH_BUTTON)

        self.wait.until(EC.url_contains("checkout-complete.html"))

        return CheckoutCompletePage(self.driver)
    
    def cancel(self) -> "InventoryPage":
        self.logger.info("Cancelling checkout")
        # Local import to avoid circular dependency
        from pages.inventory_page import InventoryPage
        self.click(CheckoutOverviewLocators.CANCEL_BUTTON)
        return InventoryPage(self.driver)