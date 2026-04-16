"""
MongoDB Setup Module
====================
Creates the marketplace database and collections if they don't exist.
Run this script once before starting the API.

Collections Created:
    - deliveries: Stores delivery tracking information
"""

from pymongo import MongoClient
import config

def create_collections():
    """
    Create required collections if they don't exist.
    Collections: deliveries
    """
    # Connect to MongoDB using config settings
    client = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
    db = client[config.MONGO_DB]

    # Create deliveries collection if it doesn't exist
    if 'deliveries' not in db.list_collection_names():
        db.create_collection('deliveries')
        print(f"Collection 'deliveries' created in '{config.MONGO_DB}'")
    else:
        print("Collection 'deliveries' already exists")

    client.close()

def setup():
    """Run full MongoDB setup."""
    create_collections()

if __name__ == "__main__":
    setup()
