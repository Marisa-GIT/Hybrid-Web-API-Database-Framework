import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from config.browsers import Browsers
from config.settings import WINDOW_MAXIMIZED, DISABLE_NOTIFICATIONS

class DriverFactory:

    @staticmethod
    def get_driver(browser):
        drivers = {
            Browsers.CHROME: DriverFactory._create_chrome_driver,
            Browsers.FIREFOX: DriverFactory._create_firefox_driver,
            Browsers.EDGE: DriverFactory._create_edge_driver,
        }

        driver_creator = drivers.get(browser)
        if driver_creator is None:
            raise ValueError(f"Unsupported browser: {browser}")

        driver = driver_creator()

        # Keeps the window maximized locally, but does not interfere with the CI environment.
        if WINDOW_MAXIMIZED and not os.getenv("CI") == "true":
            driver.maximize_window()

        return driver

    @staticmethod
    def _configure_chromium_options(options):
        if DISABLE_NOTIFICATIONS:
            options.add_argument("--disable-notifications")
        
        
        if os.getenv("CI") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")                  
            options.add_argument("--disable-dev-shm-usage")       
            options.add_argument("--disable-gpu")  
            options.add_argument("--window-size=1920,1080")       

        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            },
        )
        options.add_argument("--disable-features=PasswordLeakDetection")
        return options

    @staticmethod
    def _create_chrome_driver():
        options = DriverFactory._configure_chromium_options(
            webdriver.ChromeOptions()
        )
        return webdriver.Chrome(service=ChromeService(), options=options)

    @staticmethod
    def _create_firefox_driver():
        options = webdriver.FirefoxOptions()

        if DISABLE_NOTIFICATIONS:
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("network.dns.disableIPv6", False)
        
        if os.getenv("CI") == "true":
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        return webdriver.Firefox(service=FirefoxService(), options=options)

    @staticmethod
    def _create_edge_driver():
        options = DriverFactory._configure_chromium_options(
            webdriver.EdgeOptions()
        )
        return webdriver.Edge(service=EdgeService(), options=options)