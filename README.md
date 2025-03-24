📌 Project Plan & Architecture

🔹 Technologies & Services

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: PostgreSQL

Containerization: Docker

CI/CD Automation: GitHub Actions

Hosting Containers: Azure Container Instances (ACI)

Private Image Storage: Docker Hub (Private Repository)

Optional (for Production): Azure PostgreSQL Database

⚡ Steps to Implement

🛠️ Step 1: Set Up the Project Locally

Develop and test the application without containers.

1️⃣ Set up Python & Flask Backend.2️⃣ Configure PostgreSQL Locally.3️⃣ Develop the Frontend (HTML, CSS, JS, Bootstrap).4️⃣ Test API & Frontend Locally.

🚀 Step 2: Containerize the Application

1️⃣ Create a Dockerfile to containerize Flask, Frontend, and PostgreSQL.2️⃣ Define services using docker-compose.yml.3️⃣ Run and test the application inside Docker.

🔄 Step 3: Automate Deployment with GitHub Actions

1️⃣ Push code to GitHub (Public Repo).2️⃣ Trigger GitHub Actions on push.3️⃣ Build the Docker image locally.4️⃣ Push the image to a Private Docker Hub Repository.5️⃣ Deploy & replace the running image in Azure Container Instances (ACI).

⚙️ Setup & Installation

Prerequisites

Ensure you have the following installed:

Python: 3.11.0

Docker: 27.0.3 (Build 7d4bcd8)

Docker Compose: v2.28.1-desktop.1

Local Development Setup

# 1. Create a virtual environment
python -m venv venv

# 2. Activate the virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install flask flask_sqlalchemy psycopg2 flask-cors

# 4. Run Flask Backend
python backend/app.py

# 5. Start a simple HTTP server for frontend (Optional)
python -m http.server 8000

🐳 Docker Workflow

Building & Running the Application in Docker

# Build the Docker image
docker build -t ai-portfolio .

# Run the Docker container
docker run -p 80:80 -p 5000:5000 -p 5432:5432 ai-portfolio

🛢️ PostgreSQL Validation Commands

Connect to PostgreSQL

su - postgres
psql

List All Databases

\l

Connect to a Specific Database

\c mydb

List All Tables

\dt

Show Table Structure

\d test_table

View Data in a Table

SELECT * FROM test_table;

Exit PostgreSQL

\q


Git

git add .
git commit -m "message"
git push origin main