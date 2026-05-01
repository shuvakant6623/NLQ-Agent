import streamlit as st
import requests

st.set_page_config(page_title="MongoDB AI Agent", page_icon="🤖")

with st.sidebar:
    st.header("⚙️ Database Settings")
    st.markdown("Connect to any MongoDB database:")
    
    custom_uri = st.text_input("MongoDB URI (Leave blank for .env)", type="password", placeholder="mongodb+srv://...")
    db_name = st.text_input("Database Name", value="sample_mflix")
    collection_name = st.text_input("Collection Name", value="movies")
    
    st.info("Using the default sample data if left unchanged.")

st.title("🤖 Natural Language Database Query Agent")
st.markdown(f"Currently querying: **{db_name} > {collection_name}**")

user_question = st.text_input("Enter your question:", placeholder="e.g., When was the movie The Matrix released?")

if st.button("Ask Database"):
    if user_question:
        with st.spinner("🧠 Thinking & Searching..."):
            try:
                payload = {
                    "question": user_question,
                    "custom_uri": custom_uri,
                    "db_name": db_name,
                    "collection_name": collection_name
                }
                
                response = requests.post("http://127.0.0.1:5000/ask", json=payload)
                data = response.json()
                
                if "error" in data:
                    st.error(f"Error: {data['error']}")
                else:
                    st.success(data["answer"])
                    
            except Exception as e:
                st.error(f"Could not connect to backend. Is your Flask server running? Error: {e}")
    else:
        st.warning("Please enter a question first.")