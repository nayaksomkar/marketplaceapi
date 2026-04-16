"""
Marketplace API Configuration
============================
Centralized configuration for all modules.
Uses environment variables with fallback defaults.

Environment Variables:
    DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_NAME
    MONGODB_HOST, MONGODB_PORT, MONGODB_DATABASE
    APP_HOST, APP_PORT, APP_DEBUG, LOG_LEVEL
"""

import os

# ====================
# Database Configuration
# ====================

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USERNAME', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '0000')
DB_NAME = os.getenv('DB_NAME', 'marketplace')

# ====================
# MongoDB Configuration
# ====================

MONGO_HOST = os.getenv('MONGODB_HOST', 'localhost')
MONGO_PORT = int(os.getenv('MONGODB_PORT', 27017))
MONGO_DB = os.getenv('MONGODB_DATABASE', 'marketplace')

# ====================
# Application Configuration
# ====================

APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = int(os.getenv('APP_PORT', 5000))
DEBUG = os.getenv('APP_DEBUG', 'false').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
