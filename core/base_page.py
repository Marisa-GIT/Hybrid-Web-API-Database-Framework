from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.checkout_information_locators import CheckoutInformationLocators
from config.settings import DEFAULT_TIMEOUT
from core.logger import Logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
        self.logger = Logger.get_logger(self.__class__.__name__)

    def click(self, locator):
        self.logger.debug(f"Clicking on {locator}")
        self._find_clickable(locator).click()

    def type(self, locator, text):
        element = self._find_visible(locator)
        self.logger.debug(f"Typing into {locator}")
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        self.logger.debug(f"Clearing {locator}")
        element = self._find_visible(locator)
        element.clear()

    def get_text(self, locator):
        self.logger.debug(f"Getting text from {locator}")
        return self._find_visible(locator).text
    
    def get_attribute(self, locator, attribute):
        self.logger.debug(
            f"Getting attribute '{attribute}' from {locator}"
            )
        return self._find_visible(locator).get_attribute(attribute)

    def is_visible(self, locator):
        try:
            self._find_visible(locator)
            self.logger.debug(f"{locator} is visible")
            return True
        except TimeoutException:
            return False
        
    def is_enabled(self, locator):
        try:
            element = self._find_visible(locator)
            self.logger.debug(f"Checking if {locator} is enabled")
            return element.is_enabled()
        except TimeoutException:
            return False
        
    def is_selected(self, locator):
        try:
            element = self._find_visible(locator)
            self.logger.debug(f"Checking if {locator} is selected")
            return element.is_selected()
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        self.logger.debug(f"Scrolling to {locator}")
        element = self._find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def hover(self, locator):
        self.logger.debug(f"Hovering over {locator}")
        element = self._find_visible(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def select_by_visible_text(self, locator, text):
        self.logger.debug(f"Selecting '{text}' from dropdown {locator}")
        Select(self._find_visible(locator)).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        self.logger.debug(f"Selecting value '{value}' from dropdown {locator}")
        Select(self._find_visible(locator)).select_by_value(value)
            
    def wait_for_title(self, title_text, timeout=10):
        self.logger.debug(f"Waiting for title to be '{title_text}'")
        return WebDriverWait(self.driver, timeout).until(
            EC.title_is(title_text)
        )
    def wait_for_url(self, url_text, timeout=10):
        self.logger.debug(f"Waiting for URL to be '{url_text}'")
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url_text)
        )
     
    def get_title(self):
        self.logger.debug("Getting page title")
        return self.driver.title
    
    def get_text_from_elements(self, locator):
        self.logger.debug(f"Getting text from elements located by {locator}")
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return [element.text for element in elements]
    
    def get_element_count(self, locator):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        return len(elements)
    
    def get_elements(self, locator):
        self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def get_current_url(self):
        self.logger.debug("Getting current URL")
        return self.driver.current_url
    
    def submit_information(self) -> None:
        self.logger.info("Submitting checkout information")
        self.click(CheckoutInformationLocators.CONTINUE_BUTTON)
    
    def wait_for_url_contains(self, url_fragment, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url_fragment)
            )
        except TimeoutException as error:
            current_url = self.driver.current_url
            raise TimeoutException(
                f"Expected URL containing '{url_fragment}', "
                f"but current URL is '{current_url}'"
            ) from error
    
    def _find_visible(self, locator):
        self.logger.debug(f"Waiting for visibility of {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def _find_clickable(self, locator):
        self.logger.debug(f"Waiting for {locator} to be clickable")
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def _find_present(self, locator):
        self.logger.debug(f"Waiting for presence of {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))



