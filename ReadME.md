# Marketplace API

A simple API for marketplace data. Uses MySQL and MongoDB.

## Setup

### Docker (Easy Way)

```bash
docker-compose up -d
```

To stop:
```bash
docker-compose down
```

### Local Setup

```bash
# Create and activate venv
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Setup databases
python sqldbcreate.py
python mongodbcreate.py
python datawrite.py

# Run API
python mainapi.py
```

## Configuration

Edit `config.py`:

```python
# Database
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'your_password'
DB_NAME = 'marketplace'

# MongoDB
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'marketplace'

# App
APP_PORT = 5000
DEBUG = False
```

## Files

| File | Purpose |
|------|---------|
| `mainapi.py` | Flask API |
| `config.py` | Settings |
| `sqldbcreate.py` | MySQL setup |
| `mongodbcreate.py` | MongoDB setup |
| `datawrite.py` | Add sample data |
| `index.html` | Dashboard |
| `styles.css` | Styles |
| `app.js` | JavaScript |

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | API info |
| `/health` | Health check |
| `/api/customers` | All customers |
| `/api/customers/<id>` | Customer by ID |
| `/api/sellers` | All sellers |
| `/api/sellers/<id>` | Seller by ID |
| `/api/items` | All items |
| `/api/items/<id>` | Item by ID |
| `/api/deliveries` | All deliveries |
| `/api/deliveries/<id>` | Delivery by order ID |

## Docker Services

| Service | Port |
|---------|------|
| api | 5000 |
| mysql | 3306 |
| mongodb | 27017 |

## Sample Data

**MySQL:**
- 2 customers
- 2 sellers
- 2 items

**MongoDB:**
- 2 deliveries

## Troubleshooting

**MySQL not starting?**
```bash
# Check if MySQL is running
mysql.server start  # macOS
sudo systemctl start mysql  # Linux
```

**Port already in use?**
```bash
# Change port in config.py
APP_PORT = 5001
```
