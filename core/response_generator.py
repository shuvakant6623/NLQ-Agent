from llm.engine import ask_llm

def generate_natural_response(user_question, db_results):
    """Takes the raw database JSON and turns it into a human sentence."""
    
    system_prompt = """
    You are a friendly data assistant. 
    You will be given a user's question and the raw JSON data returned from a database.
    Your job is to answer the user's question naturally and concisely using ONLY the provided data.
    
    RULES:
    1. Do not mention the database, JSON, or queries. Just answer the question.
    2. If the database results are empty or say 'No matching records found', politely tell the user you couldn't find the information.
    3. Keep it brief. 1 or 2 sentences maximum.
    """
    
    user_prompt = f"""
    User Question: {user_question}
    
    Raw Database Results: 
    {db_results}
    """
    
    answer = ask_llm(system_prompt, user_prompt)
    return answer