# utils/database.py

import sqlite3
import os

class Database:
    def __init__(self, db_name="biospace.db"):
        self.db_name = db_name
        self.connection = None
        self._initialize_database()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            return self.connection
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=()):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_all(self, query, params=()):
        try:
            cursor = self.execute_query(query, params)
            return cursor.fetchall() if cursor else []
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def _initialize_database(self):
        # Crear las tablas iniciales si no existen
        if not os.path.exists(self.db_name):
            self.connect()
            create_experiments_table = """
                CREATE TABLE IF NOT EXISTS experiments (
                    id INTEGER PRIMARY KEY,
                    experiment_id TEXT NOT NULL,
                    name TEXT,
                    description TEXT,
                    data TEXT
                );
            """
            self.execute_query(create_experiments_table)
            self.close()