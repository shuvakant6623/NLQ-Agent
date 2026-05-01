# 🤖 NLQ-Agent: Natural Language to MongoDB

An AI-powered Microservices application that allows users to chat with a MongoDB database using natural English. 

Instead of writing complex JSON filters, users simply ask questions like *"Who directed The Matrix?"*, and the AI handles the translation, execution, and conversational response.

## 🌟 Features
* **Two-Brain AI Architecture:** Uses one LLM call for precise JSON query generation, and a second LLM call to translate raw database data into friendly English answers.
* **Microservices Design:** Separated into a Flask REST API backend and a Streamlit UI frontend.
* **Dynamic Database Switching:** Users can input their own MongoDB Atlas URI, Database Name, and Collection Name directly from the UI sidebar.
* **Benchmarking & Testing:** Includes PyTest for API validation and backend latency tracking.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Backend:** Flask, Python 3
* **Database:** MongoDB Atlas, PyMongo
* **AI Provider:** Groq (Llama-3.1-8b-instant)
* **Testing:** PyTest

## 📂 Project Structure
```text
NLQ-Agent/
├── api/
│   └── app.py                 # Flask server and API endpoints
├── core/
│   ├── executor.py            # Executes MongoDB JSON queries securely
│   ├── query_generator.py     # LLM Agent 1: English -> JSON
│   └── response_generator.py  # LLM Agent 2: JSON -> English
├── llm/
│   └── engine.py              # Groq API connection and base LLM function
├── memory/
│   └── buffer.py              # Handles conversation history & context window
├── tests/
│   └── test_api.py            # PyTest automated tests
├── ui/
│   └── app.py                 # Streamlit frontend interface
├── .env                       # Environment variables (Git-ignored)
├── config.py                  # Centralized configuration settings
└── main.py                    # Legacy terminal script
```

## 🚀 Installation & Setup

**1. Clone the repository and install dependencies:**
```bash
pip install flask streamlit requests groq pymongo python-dotenv pytest
```

**2. Setup your Environment Variables:**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/
```

**3. Run the Microservices:**
You need two terminal windows to run the frontend and backend simultaneously.

**Terminal 1 (Start the Backend API):**
```bash
python api/app.py
```

**Terminal 2 (Start the Frontend UI):**
```bash
streamlit run ui/app.py
```

## 🧪 Running Tests
To verify the API logic, run the test suite using PyTest:
```bash
pytest tests/
```