import os 
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    uri = os.getenv("MONGODB_URI")
    
    if not uri:
        raise ValueError("MongDB URI not found in environment variables")
    
    try:
        client = MongoClient(uri)
        client.admin.command('ping')
        print("Connected to MongoDb succesfully")
        return client["nlq_database"]
    
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDb: {e}")
        return None