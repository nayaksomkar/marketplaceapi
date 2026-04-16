"""
Marketplace API - Production Flask Application
"""
import os
import logging
from functools import wraps
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error as MySQLError
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import config

# Logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================
# Database Connections
# ============================================

def get_mysql_connection():
    """Create MySQL connection using config."""
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        return connection
    except MySQLError as e:
        logger.error(f"MySQL error: {e}")
        return None

def get_mongodb_client():
    """Create MongoDB connection using config."""
    try:
        client = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
        client.admin.command('ping')
        return client[config.MONGO_DB]
    except PyMongoError as e:
        logger.error(f"MongoDB error: {e}")
        return None

# ============================================
# Error Handler
# ============================================

def handle_errors(f):
    """Decorator for error handling."""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {f.__name__}: {e}")
            return jsonify({'error': str(e)}), 500
    return decorated

# ============================================
# Application Factory
# ============================================

def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    CORS(app)
    
    # Health Check
    @app.route('/health')
    def health():
        return jsonify({'status': 'ok'})

    # API Info
    @app.route('/')
    def api_info():
        return jsonify({
            'name': 'Marketplace API',
            'version': '1.0.0',
            'endpoints': [
                '/api/customers', '/api/customers/<id>',
                '/api/sellers', '/api/sellers/<id>',
                '/api/items', '/api/items/<id>',
                '/api/deliveries', '/api/deliveries/<id>'
            ]
        })

    # Customer Endpoints
    @app.route('/api/customers')
    @handle_errors
    def get_customers():
        conn = get_mysql_connection()
        if not conn:
            return jsonify({'error': 'DB connection failed'}), 503
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(result)

    @app.route('/api/customers/<int:customer_id>')
    @handle_errors
    def get_customer(customer_id):
        conn = get_mysql_connection()
        if not conn:
            return jsonify({'error': 'DB connection failed'}), 503
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return jsonify(result)
        return jsonify({'error': 'Customer not found'}), 404

    # Seller Endpoints
    @app.route('/api/sellers')
    @handle_errors
    def get_sellers():
        conn = get_mysql_connection()
        if not conn:
            return jsonify({'error': 'DB connection failed'}), 503
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sellers")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(result)

    @app.route('/api/sellers/<int:seller_id>')
    @handle_errors
    def get_seller(seller_id):
        conn = get_mysql_connection()
        if not conn:
            return jsonify({'error': 'DB connection failed'}), 503
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sellers WHERE id = %s", (seller_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return jsonify(result)
        return jsonify({'error': 'Seller not found'}), 404

    # Item Endpoints
    @app.route('/api/items')
    @handle_errors
    def get_items():
        conn = get_mysql_connection()
        if not conn:
            return jsonify({'error': 'DB connection failed'}), 503
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(result)

    @app.route('/api/items/<int:item_id>')
    @handle_errors
    def get_item(item_id):
        conn = get_mysql_connection()
        if not conn:
            return jsonify({'error': 'DB connection failed'}), 503
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return jsonify(result)
        return jsonify({'error': 'Item not found'}), 404

    # Delivery Endpoints
    @app.route('/api/deliveries')
    @handle_errors
    def get_deliveries():
        db = get_mongodb_client()
        if not db:
            return jsonify({'error': 'DB connection failed'}), 503
        deliveries = list(db.deliveries.find({}, {'_id': 0}))
        return jsonify(deliveries)

    @app.route('/api/deliveries/<int:order_id>')
    @handle_errors
    def get_delivery(order_id):
        db = get_mongodb_client()
        if not db:
            return jsonify({'error': 'DB connection failed'}), 503
        delivery = db.deliveries.find_one({'order_id': order_id}, {'_id': 0})
        if delivery:
            return jsonify(delivery)
        return jsonify({'error': 'Delivery not found'}), 404

    # Error Handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'error': 'Internal server error'}), 500

    return app

# ============================================
# Entry Point
# ============================================

if __name__ == '__main__':
    app = create_app()
    app.run(host=config.APP_HOST, port=config.APP_PORT, debug=config.DEBUG)
