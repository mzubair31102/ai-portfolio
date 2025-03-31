import os
import logging
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import AzureOpenAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG for detailed logs
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Load environment variables from .env file
load_dotenv()

# Load OpenAi_4omini API endpoint and key from environment variables
openai_4omini_endpoint = os.getenv("OPENAI_4omini_ENDPOINT")
openai_4omini_api_key = os.getenv("OPENAI_4omini_API_KEY")


# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "mydb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "admin")
        )
        logger.info("Database connection established successfully.")
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return str(e)


@app.route("/api/data")
def get_data():
    conn = get_db_connection()
    if isinstance(conn, str):
        logger.error(f"Error in DB connection: {conn}")
        return jsonify({"error": conn}), 500  # Return error if DB connection fails

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM test_table;")
        data = cur.fetchall()
        cur.close()
        conn.close()
        logger.info("Data fetched from database successfully.")
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        return jsonify({"error": "Error fetching data"}), 500


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
                {"role": "user", "content": input_text}
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model=deployment
        )

        logger.info("Received response from OpenAI API.")
        logger.debug(f"OpenAI Response: {response.choices[0].message.content}")
        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        logger.error(f"Error calling OpenAI API: {str(e)}")
        return jsonify({"error": f"Error calling OpenAI API: {str(e)}"}), 500


# Local model
def local_openai_4omini(prompt, input_text):
    url = "http://localhost:4455/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    
    data = {
        "model": "llama-3.2-1b-instruct",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": input_text}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    
    try:
        response = request.post(url, headers=headers, json=data, stream=False)

        if response.status_code == 200:
            assistant_content = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
            logger.info("Received response from local OpenAI model.")
            logger.debug(f"Local OpenAI Response: {assistant_content}")
            return {"response": assistant_content}
        else:
            logger.error(f"Error {response.status_code}: {response.text}")
            return {"error": f"Error {response.status_code}: {response.text}"}
    
    except Exception as e:
        logger.error(f"Error making local API request: {str(e)}")
        return {"error": f"Error making local API request: {str(e)}"}


@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        # Get input text from request
        data = request.get_json()
        input_text = data.get("message", "").strip()

        if not input_text:
            logger.warning("Received empty message.")
            return jsonify({"error": "Empty message"}), 400

        # System prompt
        prompt = "You are a helpful assistant, your name is Zubair."

        # Get response from OpenAI
        response = local_openai_4omini(prompt, input_text)
        return response

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # No debug mode in production
