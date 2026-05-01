from pymongo import MongoClient
import os

def execute_mongo_query(query_dict, custom_uri=None, db_name=None, collection_name=None):
    """Executes a query on a dynamic database and collection."""
    
    uri = custom_uri if custom_uri else os.getenv("MONGO_URI")
    
    if not uri:
        return "No MongoDB URI provided."
        
    try:
        client = MongoClient(uri)
        
        db_name = db_name or "sample_mflix"
        collection_name = collection_name or "movies"
        
        db = client[db_name]
        collection = db[collection_name]
        
        results = list(collection.find(query_dict, {"_id": 0}).limit(5))
        
        if not results:
            return "No matching records found."
            
        return results
        
    except Exception as e:
        return f"Database execution error: {e}"