from typing import TYPE_CHECKING
from core.base_page import BasePage
from locators.cart_locators import CartLocators
from pages.checkout_information_page import CheckoutInformationPage

if TYPE_CHECKING:
    from pages.inventory_page import InventoryPage

class CartPage(BasePage):

    def is_loaded(self) -> bool:
        return self.is_visible(CartLocators.CART_LIST)
    
    def remove_product(self, product_name: str) -> "CartPage":
        self.logger.info(
            f"Removing product '{product_name}' from cart"
            )
        remove_button_locator = CartLocators.remove_button_locator(product_name)
        self.click(remove_button_locator)
        return self
    
    def continue_shopping(self) -> "InventoryPage":
        self.logger.info("Continuing shopping")
        # Local import to avoid circular dependency
        from pages.inventory_page import InventoryPage
        self.click(CartLocators.CONTINUE_SHOPPING_BUTTON)
        return InventoryPage(self.driver)
    
    def checkout(self) -> "CheckoutInformationPage":
        self.logger.info("Proceeding to checkout")
        self.click(CartLocators.CHECKOUT_BUTTON)
        self.wait_for_url_contains("checkout-step-one.html")
        return CheckoutInformationPage(self.driver)
    
    def has_product(self, product_name: str) -> bool:
        return self.is_visible(CartLocators.product_locator(product_name))
    
    def get_product_name(self, product_name: str) -> str:
        self.logger.info(f"Getting name for product '{product_name}'")
        product_locator = CartLocators.product_locator(product_name)
        return self.get_text(product_locator)
    
    def get_product_names(self) -> list[str]:
        self.logger.info("Getting product names in the cart")
        product_elements = CartLocators.PRODUCT_NAMES
        return self.get_text_from_elements(product_elements)

    def get_product_price(self, product_name: str) -> str:
        self.logger.info(f"Getting price for product '{product_name}'")
        price_locator = CartLocators.product_price_locator(product_name)
        return self.get_text(price_locator)

    def get_product_prices(self) -> list[str]:
        self.logger.info("Getting product prices in the cart")
        price_elements = CartLocators.PRODUCT_PRICES
        return self.get_text_from_elements(price_elements)

    def get_product_count(self) -> int:
        return self.get_element_count(CartLocators.CART_LIST)

    
