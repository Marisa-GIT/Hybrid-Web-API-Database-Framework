from selenium.webdriver.common.by import By

class InventoryLocators:
    
    @staticmethod
    def _inventory_list_container() -> tuple:
        return (By.XPATH, "//div[@class='inventory_list']")

    @staticmethod
    def _product_container(product_name: str) -> tuple:
        return (
            By.XPATH,
            f"//div[normalize-space()='{product_name}']/ancestor::div[@class='inventory_item']"
        )

    @staticmethod
    def get_add_to_cart_button_locator(product_name: str) -> tuple:
        _, container = InventoryLocators._product_container(product_name)
        return (
            By.XPATH,
            f"{container}//button[contains(@class, 'btn_inventory')]"
        )

    @staticmethod
    def get_remove_button_locator(product_name: str) -> tuple:
        _, container = InventoryLocators._product_container(product_name)
        return (
            By.XPATH,
            f"{container}//button[text()='Remove']"
        )
    
    @staticmethod
    def get_product_price_locator(product_name: str) -> tuple:
        _, container = InventoryLocators._product_container(product_name)
        return (
            By.XPATH,
            f"{container}//div[@class='inventory_item_price']"
        )

    @staticmethod
    def get_product_name_locator(product_name: str) -> tuple:
        _, container = InventoryLocators._product_container(product_name)
        return (
            By.XPATH,
            f"{container}//div[normalize-space()='{product_name}']"
        )

    @staticmethod
    def get_all_product_names_locator() -> tuple:
        _, container = InventoryLocators._inventory_list_container()
        return (
            By.XPATH,
            f"{container}//div[contains(@class, 'inventory_item_name')]"
        )

    @staticmethod
    def get_all_product_prices_locator() -> tuple:
        _, container = InventoryLocators._inventory_list_container()
        return (
            By.XPATH,
            f"{container}//div[@class='inventory_item_price']"
        )

    @staticmethod
    def get_page_title_locator() -> tuple:
        return (By.CLASS_NAME, "title")

    @staticmethod
    def get_cart_icon_locator() -> tuple:
        return (By.CLASS_NAME, "shopping_cart_link")

    @staticmethod
    def get_cart_badge_locator() -> tuple:
        return (By.CLASS_NAME, "shopping_cart_badge")
    
    @staticmethod
    def get_sort_dropdown_locator() -> tuple:
        return (By.CLASS_NAME, "product_sort_container")