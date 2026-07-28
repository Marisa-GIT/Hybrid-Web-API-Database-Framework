import os
import pytest
from config.settings import BASE_URL, BROWSER
from core.driver_factory import DriverFactory
from utils.test_data_manager import TestDataManager
from api.services.user_service import UserAPIClient
from pages.login_page import LoginPage
from datetime import datetime
import pytest

from database.repositories.user_repository import UserRepository

@pytest.fixture
def driver():

    """Creates and disposes the WebDriver instance."""

    driver = DriverFactory.get_driver(BROWSER)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):

    def _login(user_type="standard_user"):
        login_page = LoginPage(driver)

        user = TestDataManager.get_user(user_type)

        return login_page.login(
            user["username"],
            user["password"]
        )

    return _login

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call):
    
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return
        
        timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
        )
        
        os.makedirs("screenshots", exist_ok=True)

        driver.save_screenshot(
        f"screenshots/{item.name}_{timestamp}.png"
        )

@pytest.fixture
def user_api_client():
    client = UserAPIClient()
    yield client
    client.close()

@pytest.fixture
def user_repository():
    repository = UserRepository()

    yield repository

    repository.close()