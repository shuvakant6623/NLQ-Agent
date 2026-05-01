from db.connection import get_db_connection

def seed_database():
    db = get_db_connection()

    if db is None:
        return 
    
    collection = db["employee"]

    collection.delete_many({})

    sample_data = [
        {"name": "Alice", "age": 30, "department": "HR"},
        {"name": "Bob", "age": 25, "department": "Engineering"},
        {"name": "Charlie", "age": 35, "department": "Sales"},
    ]

    collection.insert_many(sample_data)

if __name__ == "__main__":
    seed_database()