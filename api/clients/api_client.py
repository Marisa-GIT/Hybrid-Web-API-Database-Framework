import requests
import logging
from config.environment import API_BASE_URL


class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or API_BASE_URL
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        
        # Default headers for all requests
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint, **kwargs):
        """Wrapper method for centralized GET requests"""
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", 10)
        return self.session.get(url, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        """Wrapper method for centralized POST requests"""
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json, **kwargs)

    def close(self):
        """Close the requests session"""
        self.session.close()


