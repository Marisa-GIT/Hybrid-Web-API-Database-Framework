from pages.login_page import LoginPage
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

    def validate_user_consistency(self, user_id):
            """Retrieve the same user from the API and the database."""
    
            api_user = self.get_api_user(user_id)
            db_user = self.get_database_user(user_id)
    
            return api_user, db_user