from db.connection import get_db_connection

def execute_mongo_query(query_dict):
    db = get_db_connection()

    if db is None:
        return {"error": "Failed to connect to the database"}
    
    collection = db['employees']

    try:
        results = list(collection.find(query_dict, {"_id": 0}))

        if not results:
            return {"message": "No matching records found"}
        
        return {"results": results}
    except Exception as e:
        return {"error": f"An error occurred while executing the query: {str(e)}"}