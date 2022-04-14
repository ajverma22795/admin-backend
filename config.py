from pymongo import MongoClient
from datetime import datetime

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DB_NAME = 'adminDB'
client = MongoClient(MONGO_HOST,MONGO_PORT)
if 'user' not in client[DB_NAME].list_collection_names():
    USER_COLLECTION = client[DB_NAME]['user']
    USER_COLLECTION.create_index('userId', unique = True)
USER_COLLECTION = client[DB_NAME]['user']

if 'admin' not in client[DB_NAME].list_collection_names():
    ADMIN_COLLECTION = client[DB_NAME]['admin']
    ADMIN_COLLECTION.create_index('adminId', unique = True)
ADMIN_COLLECTION = client[DB_NAME]['admin']
