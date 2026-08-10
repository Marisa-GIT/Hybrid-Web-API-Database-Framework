from pages.login_page import LoginPage
from services.validators.hybrid_validator import HybridValidator
class HybridService:
    """Coordinates UI, API, and Database workflows."""

    def __init__(self, driver, user_api_client, user_repository):
            self.driver = driver
            self.user_api_client = user_api_client
            self.user_repository = user_repository

    def login_user(self, username, password):
        login_page = LoginPage(self.driver)
        return login_page.login(username, password)

    def get_api_user(self, user_id):
        """Retrieve a user from the API."""
        response = self.user_api_client.get_user_by_id(user_id)
        return response.json()

    def get_database_user(self, user_id):
        """Retrieve a user from the database."""
        return self.user_repository.get_user_by_id(user_id)

    def validate_user_flow(self, user_id):
        """Validate that the user flow is successful across API and Database."""

        api_user = self.get_api_user(user_id)
        db_user = self.get_database_user(user_id)

        HybridValidator.assert_user_flow(
            api_user=api_user,
            db_user=db_user,
            expected_user_id=user_id
        )

        return {
            "api_user": api_user,
            "db_user": db_user
        }

    def login_and_validate_user(self, username, password, user_id):
        """
        Perform login through the UI and validate the user
        across API and Database.
        """

        inventory_page = self.login_user(username, password)

        validation = self.validate_user_flow(user_id)

        return {
            "inventory_page": inventory_page,
            "validation": validation
        }
    
    def add_product_to_cart(self, username, password, product_name):
        """
        Login and add a product to the shopping cart.
        """

        inventory_page = self.login_user(
            username,
            password
        )

        inventory_page.add_product_to_cart(product_name)

        return inventory_page.open_cart()