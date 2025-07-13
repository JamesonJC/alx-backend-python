import sqlite3 
import functools
from datetime import datetime

def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        #try:
        results = func(conn, *args, **kwargs)
        #finally:
        conn.close()
        # if conn.close:
        #     print("Database connection closed.")
        # else:
        #     print("Database connection was not closed properly.")
        return results
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 

#### Fetch user by ID with automatic connection handling 
user = get_user_by_id(user_id=1)
print(user)