
import sqlite3
#import functools

#### decorator to log SQL queries ####

def log_queries(func):
    def wrapper(*args, **kwargs):
        # Get the query from the first argument or kwargs
        # query = kwargs.get('query', '')
        print(f"Executing query: {kwargs}")
        return func(*args, **kwargs)
    
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    # print(f"Executing query: {query}")
    # for row in results:
    #     print(row)
    # conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")