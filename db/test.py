from db.connection import get_db_connection

db = get_db_connection()

if db is not None:
    print(f"Successfully connected to the database: {db.name}")