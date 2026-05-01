from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.query_generator import generate_mongo_query
from core.executor import execute_mongo_query
from core.response_generator import generate_natural_response

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_agent():
    data = request.json
    
    user_question = data.get("question")
    custom_uri = data.get("custom_uri", "")
    db_name = data.get("db_name", "sample_mflix")
    collection_name = data.get("collection_name", "movies")
    
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    mongo_query = generate_mongo_query(user_question, db_name, collection_name)
    if not mongo_query:
        return jsonify({"error": "Failed to generate query"}), 500
        
    try:
        raw_results = execute_mongo_query(mongo_query, custom_uri, db_name, collection_name)
        
        human_answer = generate_natural_response(user_question, raw_results)
        
        return jsonify({
            "query": mongo_query,
            "results": raw_results,
            "answer": human_answer 
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)