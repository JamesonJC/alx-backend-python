#!/usr/bin/env python3
import sqlite3
from contextlib import contextmanager
class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params is not None else ()

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute(self):
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()
    
def main():
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery("users.db", query, params) as executor:
        results = executor.execute()
        for row in results:
            print(row)