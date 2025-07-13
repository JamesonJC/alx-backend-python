
import sqlite3
import functools
from datetime import datetime

#### decorator to log SQL queries ####
def add(*a, b):
    pass

def log_queries(func):
    """Decorator to log SQL queries executed by the function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        my_query = kwargs
        print(f"Executed query: {my_query}")

        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    # print(f"Executing query: {query}")
    #for row in results:
    #     print(row)
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
#for row in  users:
#     print(row)
