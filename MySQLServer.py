# MySQLServer.py

import mysql.connector
import json
from dotenv import load_dotenv

load_dotenv()
from mysql.connector import errorcode

def main():
    try:
        # 1. Open connection to MySQL server (no database specified)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Selekta@2024'
        )
        cursor = conn.cursor()

        # 2. Try creating the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            # Error code 1007: Can't create database; database exists
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                # Database already exists — script continues without failure
                pass
            else:
                # Any other error during creation
                print(f"Failed creating database: {err}")
        finally:
            # 3. Clean up cursor and connection
            cursor.close()
            conn.close()

    except mysql.connector.Error as conn_err:
        # Handle errors when failing to connect to the server
        print(f"Error connecting to MySQL: {conn_err}")

if __name__ == "__main__":
    main()
