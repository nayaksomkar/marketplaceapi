"""
Data Seeding Module
===================
Seeds sample data into MySQL and MongoDB databases.
Safe to run multiple times - checks for existing data before inserting.
"""

import mysql.connector
from pymongo import MongoClient
from datetime import datetime
import config

def seed_mysql():
    """
    Insert sample data into MySQL tables.
    Only inserts if data doesn't already exist (idempotent).
    """
    connection = mysql.connector.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    cursor = connection.cursor()

    # Sample customers
    cursor.execute("SELECT * FROM customers WHERE email = 'john@example.com'")
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO customers (name, email, address) VALUES
            ('John Doe', 'john@example.com', '123 Main St')
        """)

    cursor.execute("SELECT * FROM customers WHERE email = 'jane@example.com'")
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO customers (name, email, address) VALUES
            ('Jane Smith', 'jane@example.com', '456 Elm St')
        """)

    # Sample sellers
    cursor.execute("SELECT * FROM sellers WHERE email = 'bob@example.com'")
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO sellers (name, email, business_name) VALUES
            ('Bob Johnson', 'bob@example.com', 'Bob''s Electronics')
        """)

    cursor.execute("SELECT * FROM sellers WHERE email = 'alice@example.com'")
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO sellers (name, email, business_name) VALUES
            ('Alice Brown', 'alice@example.com', 'Alice''s Apparel')
        """)

    # Sample items
    cursor.execute("SELECT * FROM items WHERE name = 'Laptop' AND seller_id = 1")
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO items (name, description, price, seller_id) VALUES
            ('Laptop', 'High-performance laptop', 999.99, 1)
        """)

    cursor.execute("SELECT * FROM items WHERE name = 'T-shirt' AND seller_id = 2")
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO items (name, description, price, seller_id) VALUES
            ('T-shirt', 'Cotton t-shirt', 19.99, 2)
        """)

    connection.commit()
    cursor.close()
    connection.close()
    print("MySQL data seeded")

def seed_mongodb():
    """
    Insert sample data into MongoDB deliveries collection.
    Only inserts if order_id doesn't already exist (idempotent).
    """
    client = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
    db = client[config.MONGO_DB]
    deliveries = db.deliveries

    # Sample delivery: In Transit
    if deliveries.count_documents({"order_id": 1}) == 0:
        deliveries.insert_one({
            "order_id": 1,
            "status": "In Transit",
            "location": {"lat": 40.7128, "lon": -74.0060},
            "timestamp": datetime.now()
        })

    # Sample delivery: Delivered
    if deliveries.count_documents({"order_id": 2}) == 0:
        deliveries.insert_one({
            "order_id": 2,
            "status": "Delivered",
            "location": {"lat": 34.0522, "lon": -118.2437},
            "timestamp": datetime.now()
        })

    client.close()
    print("MongoDB data seeded")

def seed_all():
    """Seed all databases (MySQL and MongoDB)."""
    seed_mysql()
    seed_mongodb()
    print("All data seeded successfully")

if __name__ == "__main__":
    seed_all()
