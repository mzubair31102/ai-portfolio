import logging
from flask import Flask, jsonify, request
import os
import psycopg2
from flask_cors import CORS
from openai import AzureOpenAI
from dotenv import load_dotenv
from services.search_url import duckduckgo_search
from services.scraper import get_text_from_url

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Load environment variables from .env file
load_dotenv()

# Load OpenAi_4omini API endpoint and key from environment variables
openai_4omini_endpoint = os.getenv("OPENAI_4omini_ENDPOINT")
openai_4omini_api_key = os.getenv("OPENAI_4omini_API_KEY")

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # This will log debug info to stdout
logger = logging.getLogger(__name__)

# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "mydb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "admin")
        )
        logger.debug("Database connection successful")
        return conn
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}")
        return str(e)

@app.route("/api/data")
def get_data():
    conn = get_db_connection()
    if isinstance(conn, str):
        logger.error(f"DB Connection Error: {conn}")
        return jsonify({"error": conn}), 500  # Return error if DB connection fails

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM test_table;")
        data = cur.fetchall()
        cur.close()
        conn.close()
        logger.debug("Data fetched successfully")
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        return jsonify({"error": "Failed to fetch data"}), 500

def openai_4omini(prompt, input_text):
    try:
        endpoint = openai_4omini_endpoint
        model_name = "gpt-4o-mini"
        deployment = "ai-portfolio-gpt-4o-mini"

        subscription_key = openai_4omini_api_key
        api_version = "2024-12-01-preview"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=subscription_key,
        )

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": input_text},
            ],
            max_tokens=1000,
            temperature=0.5,
            top_p=0.5,
            model=deployment,
        )

        logger.debug(f"OpenAI response: {response.choices[0].message.content}")
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        logger.error(f"OpenAI error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        logger.debug(f"Received data: {data}")
        input_text = data.get("message", "").strip()
        session_id = data.get("sessionId", None)
        logger.debug(f"Session ID: {session_id}")
        if not input_text:
            logger.error("Empty message received")
            return jsonify({"error": "Empty message"}), 400

        prompt = "You are a helpful assistant your name is Zubair."
        response = openai_4omini(prompt, input_text)
        return response
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/search", methods=["POST"])
def search():
    try:
        data = request.get_json()
        input_text = data.get("message", "").strip()
        
        if not input_text:
            logger.error("Empty message received")
            return jsonify({"error": "Empty message"}), 400
        
        prompt = "You are a helpful assistant your name is Zubair."
        response = openai_4omini(prompt, input_text)
        return response
    except Exception as e:
        logger.error(f"Search error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Exposed for container
