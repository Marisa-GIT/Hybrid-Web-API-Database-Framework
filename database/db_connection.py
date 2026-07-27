import mysql.connector

from config.environment import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

class DatabaseConnection:

    def __init__(self):
        def __init__(self):
            self.host = DB_HOST
            self.port = DB_PORT
            self.database = DB_NAME
            self.user = DB_USER
            self.password = DB_PASSWORD

            self.connection = None
            self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

        self.cursor = self.connection.cursor(dictionary=True)

        return self.connection

    def get_cursor(self):
        if self.connection is None or not self.connection.is_connected():
            self.connect()

        return self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection and self.connection.is_connected():
            self.connection.close()