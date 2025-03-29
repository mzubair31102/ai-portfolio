from flask import Flask, jsonify, request
import os
import psycopg2
from flask_cors import CORS
from openai import AzureOpenAI
from dotenv import load_dotenv

app = Flask(__name__)

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}}, max_age=600)  # Cache preflight for 10 minutes

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API credentials
openai_4omini_endpoint = os.getenv("OPENAI_4omini_ENDPOINT")
openai_4omini_api_key = os.getenv("OPENAI_4omini_API_KEY")

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "mydb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "admin")
        )
        return conn
    except Exception as e:
        return None, str(e)  # Return None if connection fails, along with an error message

@app.route("/api/data")
def get_data():
    conn, error = get_db_connection()
    if error:
        return jsonify({"error": error}), 500  # Return error if DB connection fails

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM test_table;")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle unexpected errors

# Function to communicate with OpenAI
def openai_4omini(prompt, input_text):
    try:
        client = AzureOpenAI(
            api_version="2024-12-01-preview",
            azure_endpoint=openai_4omini_endpoint,
            api_key=openai_4omini_api_key,
        )

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": input_text},
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model="ai-portfolio-gpt-4o-mini",
        )

        return response.choices[0].message.content  # Return plain response content
    except Exception as e:
        return str(e)  # Return error as a string for proper handling

@app.route("/api/chat", methods=["GET"])
def chat():
    try:
        # Get input text from request
        input_text = request.args.get("message", "").strip()

        if not input_text:
            return jsonify({"error": "Empty message"}), 400
        
        # System prompt
        prompt = "You are a helpful assistant. Your name is Zubair."
        
        # Get response from OpenAI
        response = openai_4omini(prompt, input_text)

        if isinstance(response, str) and response.startswith("Error"):
            return jsonify({"error": response}), 500  # Handle OpenAI errors

        return jsonify({"response": response})  # Return the processed response
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle unexpected errors

if __name__ == "__main__":
    app.run(debug=True)  # Remove debug=True in production
