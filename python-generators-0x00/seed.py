#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import csv
import uuid

# Connect to MySQL server
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# Create database if it doesn't exist
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

# Connect to the ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='ALX_prodev',
            password='alx',
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

# Create the user_data table
def create_table(connection):
    cursor = connection.cursor()
    table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL
    );
    """
    try:
        cursor.execute(table_query)
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
    finally:
        cursor.close()

# Insert data into the table from CSV
def insert_data(connection, filename):
    cursor = connection.cursor()
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                user_id = row.get('user_id') or str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                
                insert_query = """
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s);
                """
                cursor.execute(insert_query, (user_id, name, email, age))
        connection.commit()
        print("Data inserted successfully from CSV")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    finally:
        cursor.close()
