from database.db_connection import DatabaseConnection
import logging


class BaseRepository:

    def __init__(self):
        self.db = DatabaseConnection()
        self.logger = logging.getLogger(__name__)

    def get_cursor(self):
        return self.db.get_cursor()

    def close(self):
        self.db.close()