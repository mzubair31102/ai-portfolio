from flask import Flask, jsonify,request
import os
import psycopg2
from flask_cors import CORS
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Load environment variables from .env file
load_dotenv()

#Load OpenAi_4omini api endpoint and key from environment variables
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
        return conn
    except Exception as e:
        return str(e)

@app.route("/api/data")
def get_data():
    conn = get_db_connection()
    if isinstance(conn, str):
        return jsonify({"error": conn}), 500  # Return error if DB connection fails

    cur = conn.cursor()
    cur.execute("SELECT * FROM test_table;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

def openai_4omini(prompt, input_text):
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
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": input_text,
            }
        ],
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
        model=deployment
    )

    print(response.choices[0].message.content)
    return jsonify({"response": response.choices[0].message.content})

@app.route("/api/chat", methods=["POST"])
def chat():
    return jsonify({"response": "Hello from the chat endpoint!"})
# def chat():
#     try:
#         # Get input text from request
#         data = request.get_json()
#         input_text = data.get("message", "").strip()
        
#         if not input_text:
#             return jsonify({"error": "Empty message"}), 400
        
#         # System prompt
#         prompt = "You are a helpful assistant your name is Zubair."
        
#         # Get response from OpenAI
#         response = openai_4omini(prompt, input_text)
#         return response
        
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)  # No debug mode in production
