from selenium.webdriver.common.by import By

class CheckoutCompleteLocators:
    COMPLETE_CONTAINER  = (By.CLASS_NAME, "checkout_complete_container")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")