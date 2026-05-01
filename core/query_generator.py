import json
from llm.engine import ask_llm
from memory.buffer import add_to_history, get_history_context

MONGO_SCHEMA = """
Collection: employees
Fields:
- name (string)
- role (string)
- salary (integer)
"""

def generate_mongo_query(user_question):
    past_context = get_history_context()
    
    system_prompt = """
    You are a strict AI assistant that converts natural language into MongoDB query filters.
    You will be provided with a user's question, previous conversation history, and the database schema.
    
    Use the conversation history to figure out pronouns like 'he', 'she', or 'they'.

    CRITICAL RULES:
    1. Do NOT write SQL. Write MongoDB JSON filters (e.g., {"salary": {"$gt": 50000}}).
    2. ONLY output the raw JSON object. Do not add markdown blocks.
    3. Do not add any conversational text.
    """
    
    user_prompt = f"""
    Previous Questions:
    {past_context}
    
    Current Question: {user_question}
    
    Database Schema:
    {MONGO_SCHEMA}
    """
    
    raw_response = ask_llm(system_prompt, user_prompt)
    
    add_to_history(user_question)
    
    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        print("AI returned invalid JSON:", raw_response)
        return None