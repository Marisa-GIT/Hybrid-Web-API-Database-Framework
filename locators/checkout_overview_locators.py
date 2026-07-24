from selenium.webdriver.common.by import By

class CheckoutOverviewLocators:
    
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    OVERVIEW_CONTAINER = (By.ID, "checkout_summary_container")