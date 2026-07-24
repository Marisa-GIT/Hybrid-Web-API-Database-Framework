from selenium.webdriver.common.by import By

class CartLocators:
    CART_LIST = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    @staticmethod
    def remove_button_locator(product_name: str):
        return (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'cart_item')]"
            "//button[contains(@class, 'btn') and contains(@class, 'btn_secondary')]"
        )

    @staticmethod
    def product_locator(product_name: str):
        return (
            By.XPATH,
            f"//div[contains(@class, 'inventory_item_name') and normalize-space()='{product_name}']"
        )

    @staticmethod
    def product_price_locator(product_name: str):
        return (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'cart_item')]"
            "//div[contains(@class, 'inventory_item_price')]"
        )