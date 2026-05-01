import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

database_schema = """
Table: employee
Columns:
- name (string)
- age (integer)
- department (string)
"""

def ask_llm(user_input):
    try:
        response = groq_client.chat.completions.create (
            model = "llama3-8b-8192",
            messages = [
                {"role": "System",
                 "content": "You are a helpful AI assistant that helps users to query a database using natural language. You will be provided with the user's question and the database schema to understand the structure of the database. Your task is to generate a JSON format query that can be executed on the database to retrieve the similar or relevant information based on the user's question and the database schema. Always generate JSON format queries that are syntactically correct and can be executed without errors. If the user's question is ambiguous, ask for clarification before generating the JSON format query."},
                {"role": "User",
                 "content": f"User's Question: {user_input}\n\nDatabase Schema: {database_schema}"
                }
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error while generating JSON query: {e}")
        return None
    
if __name__ == "__main__":
    user_question = "What are the names of employees in the HR department?"
    json_query = ask_llm(user_question)
    print("Generated JSON Query:")
    print(json_query)