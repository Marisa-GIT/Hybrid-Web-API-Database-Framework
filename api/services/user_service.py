from api.client import APIClient
from api.endpoints import UserEndpoints

class UserAPIClient(APIClient):
    
    def __init__(self, base_url=None):
        super().__init__(base_url=base_url)

    def get_all_users(self):
        self.logger.info("GET /users")
        response = self.get(UserEndpoints.USERS)
        self.logger.info(f"GET {response.url} - {response.status_code}")
        return response

    def get_user_by_id(self, user_id):
        endpoint = UserEndpoints.USER_BY_ID.format(id=user_id)
        self.logger.info(f"GET /users/{user_id}")
        response = self.get(endpoint)
        self.logger.info(f"GET {response.url} - {response.status_code}")
        return response