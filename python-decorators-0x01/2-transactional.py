import sqlite3 
import functools
from datetime import datetime

def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        conn = sqlite3.connect('users.db')
        try:
            args = (conn, *args)
            result = func(*args, **kwargs)
        finally:
            conn.close()
        #if conn.close:
        #    print("Database connection closed.")
        return result
    return wrapper

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"An error occurred: {e}")
    return wrapper

def checks

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=10, new_email='Crawford_Cartwright@hotmail.com')