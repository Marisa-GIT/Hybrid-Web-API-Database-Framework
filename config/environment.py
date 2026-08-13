import os

from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv("BASE_URL")

API_BASE_URL = os.getenv("API_BASE_URL")

DB_HOST = os.getenv("DB_HOST")

DB_PORT = int(os.getenv("DB_PORT", "3306"))

DB_NAME = os.getenv("DB_NAME")

DB_USER = os.getenv("DB_USER")

DB_PASSWORD = os.getenv("DB_PASSWORD")

ROOT_PASSWORD = os.getenv("DB_ROOT_PASSWORD")
