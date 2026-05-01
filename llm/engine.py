import os
import json
from dotenv import load_dotenv
from groq import Groq
from pymongo import MongoClient

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

mongo_client = MongoClient(os.getenv("MONGODB_URI"))
db = mongo_client[os.getenv("DB_NAME", "test_db")]
collection = db["employee"]

database_schema = """
Table: employee
Columns:
- name (string)
- age (integer)
- department (string)
"""

def ask_llm(user_input):
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "Convert the user query into a valid MongoDB JSON query using the given schema. Return only JSON."
            },
            {
                "role": "user",
                "content": f"User Question: {user_input}\n\nDatabase Schema: {database_schema}"
            }
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    ask_llm()