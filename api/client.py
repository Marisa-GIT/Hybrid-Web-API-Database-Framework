import requests
from config.environment import API_BASE_URL
from api.client import APIClient
from core import logger
from api.endpoints import UserEndpoints
class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or API_BASE_URL
        self.session = requests.Session()
        
        # Headers por defecto para todas las peticiones
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint, **kwargs):
        """Método wrapper para peticiones GET centralizadas"""
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", 10)
        return self.session.get(url, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        """Método wrapper para peticiones POST centralizadas"""
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json, **kwargs)

    def close(self):
        """Cierra la sesión de requests"""
        self.session.close()


class UserAPIClient(APIClient):
    
    def __init__(self, base_url=None):
        super().__init__(base_url=base_url)

    def get_all_users(self):
        logger.info("GET /users")
        response = self.get(UserEndpoints.USERS)
        logger.info(f"GET {response.url} - {response.status_code}")
        return response

    def get_user_by_id(self, user_id):
        endpoint = UserEndpoints.USER_BY_ID.format(id=user_id)
        logger.info(f"GET /users/{user_id}")
        response = self.get(endpoint)
        logger.info(f"GET {response.url} - {response.status_code}")
        return response