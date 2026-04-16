"""
MySQL Database Setup Module
"""
import mysql.connector as con
import config

def create_database():
    """Create marketplace database if it doesn't exist."""
    connection = con.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME}")
    print(f"Database '{config.DB_NAME}' ready")
    cursor.close()
    connection.close()

def create_tables():
    """Create all required tables if they don't exist."""
    connection = con.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            address VARCHAR(255)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sellers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            business_name VARCHAR(100)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            description TEXT,
            price DECIMAL(10, 2),
            seller_id INT,
            FOREIGN KEY (seller_id) REFERENCES sellers(id)
        )
    """)

    print("Tables created successfully")
    cursor.close()
    connection.close()

def setup():
    """Run full database setup."""
    create_database()
    create_tables()

if __name__ == "__main__":
    setup()
