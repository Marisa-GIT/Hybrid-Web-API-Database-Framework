
from typing import TYPE_CHECKING
from core.base_page import BasePage
from locators.checkout_information_locators import CheckoutInformationLocators
from pages.checkout_overview_page import CheckoutOverviewPage


if TYPE_CHECKING:
    from pages.cart_page import CartPage
    


class CheckoutInformationPage(BasePage):

    def is_loaded(self) -> bool:
        return (
            self.is_visible(CheckoutInformationLocators.FIRST_NAME)
            and self.is_visible(CheckoutInformationLocators.LAST_NAME)
            and self.is_visible(CheckoutInformationLocators.POSTAL_CODE)
            and self.is_visible(CheckoutInformationLocators.CONTINUE_BUTTON)
        )
    
    def fill_first_name(self, first_name: str) -> "CheckoutInformationPage":
        self.logger.info(f"Filling in first name: {first_name}")
        self.type(CheckoutInformationLocators.FIRST_NAME, first_name)
        return self
    
    def fill_last_name(self, last_name: str) -> "CheckoutInformationPage":
        self.logger.info(f"Filling in last name: {last_name}")
        self.type(CheckoutInformationLocators.LAST_NAME, last_name)
        return self

    def fill_postal_code(self, postal_code: str) -> "CheckoutInformationPage":
        self.logger.info(f"Filling in postal code: {postal_code}")
        self.type(CheckoutInformationLocators.POSTAL_CODE, postal_code)
        return self

    def complete_information(self, first_name: str, last_name: str, postal_code: str) -> "CheckoutInformationPage":
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)
        return self
    
    def get_error_message(self) -> str | None:
        errors = self.get_elements(
            CheckoutInformationLocators.ERROR_MESSAGE
        )
        return errors[0].text if errors else None
    
    def submit_information(self) -> None:
        self.logger.info("Submitting checkout information")
        self.click(CheckoutInformationLocators.CONTINUE_BUTTON)
        return CheckoutOverviewPage(self.driver)


    def cancel(self) -> "CartPage":
        self.logger.info("Cancelling checkout and returning to cart")
        # Local import to avoid circular dependency
        from pages.cart_page import CartPage
        self.click(CheckoutInformationLocators.CANCEL_BUTTON)
        return CartPage(self.driver)