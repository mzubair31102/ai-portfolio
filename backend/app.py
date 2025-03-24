from flask import Flask, jsonify
import os
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

if __name__ == "__main__":
    app.run(debug=True)  # No debug mode in production
