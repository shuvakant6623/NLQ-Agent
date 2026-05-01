import json
from llm.engine import ask_llm

def generate_mongo_query(user_question, db_name, collection_name):
    system_prompt = f"""
    You are a strict AI assistant that converts natural language into MongoDB query filters.
    Target Database: {db_name}
    Target Collection: {collection_name}

    CRITICAL RULES:
    1. Write MongoDB JSON filters (e.g., {{"year": 2001}} or {{"title": "The Matrix"}}).
    2. ONLY output the raw JSON object. Do not add markdown blocks like ```json ... ```.
    3. Do not add any conversational text.
    4. Make text searches case-insensitive if possible, using regex: {{"title": {{"$regex": "avatar", "$options": "i"}}}}
    """
    
    user_prompt = f"User's Question: {user_question}"
    
    raw_response = ask_llm(system_prompt, user_prompt)
    
    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        print("AI returned invalid JSON:", raw_response)
        return None