# Marketplace API

A RESTful API for marketplace data management with MySQL and MongoDB.

## Quick Start

### Docker
```bash
docker-compose up -d
```

### Local Development
```bash
# Setup virtual environment
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Setup databases (creates tables automatically)
python sqldbcreate.py
python mongodbcreate.py
python datawrite.py

# Run API
python mainapi.py

# Open index.html in browser
```

## Configuration

All configuration is managed in `config.py`. Default values:

```python
# Database
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = '0000'
DB_NAME = 'marketplace'

# MongoDB
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'marketplace'

# App
APP_HOST = '0.0.0.0'
APP_PORT = 5000
DEBUG = False
LOG_LEVEL = 'INFO'
```

Override with environment variables:

```bash
export DB_HOST=localhost
export DB_PORT=3306
export DB_USER=root
export DB_PASSWORD=your_secure_password
export DB_NAME=marketplace
export MONGO_HOST=localhost
export MONGO_PORT=27017
export MONGO_DB=marketplace
export APP_PORT=5000
export DEBUG=false
export LOG_LEVEL=INFO
```

Or create `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
# Edit .env with your values
```

## Project Files

| File | Purpose |
|------|---------|
| `mainapi.py` | Flask API server |
| `config.py` | Configuration settings |
| `sqldbcreate.py` | Creates MySQL tables |
| `mongodbcreate.py` | Creates MongoDB collections |
| `datawrite.py` | Seeds sample data |
| `index.html` | Dashboard UI |
| `styles.css` | Dashboard styles |
| `app.js` | Dashboard logic |

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| GET `/` | API info |
| GET `/health` | Health check |
| GET `/api/customers` | List customers |
| GET `/api/customers/<id>` | Get customer |
| GET `/api/sellers` | List sellers |
| GET `/api/sellers/<id>` | Get seller |
| GET `/api/items` | List items |
| GET `/api/items/<id>` | Get item |
| GET `/api/deliveries` | List deliveries |
| GET `/api/deliveries/<id>` | Get delivery |

## Docker Services

| Service | Port |
|---------|------|
| api | 5000 |
| mysql | 3306 |
| mongodb | 27017 |

## Project Structure

```
marketplaceapi/
├── mainapi.py
├── config.py
├── sqldbcreate.py
├── mongodbcreate.py
├── datawrite.py
├── index.html
├── styles.css
├── app.js
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```
