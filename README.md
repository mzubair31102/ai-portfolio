# AI Chatbot & Assistant Template with Azure AI Foundry | Full Azure Deployment

![Project Architecture](https://github.com/user-attachments/assets/dd797592-ce70-47ac-961f-b445b4f497f0)

## 🚀 Project Overview

This project is a **fully functional AI Chatbot & Assistant template**, built with **Azure AI Foundry** for AI model integration and **full deployment on Azure**. It provides a complete, end-to-end solution for developers who want to quickly launch AI-driven applications on the cloud.

### Key Highlights

- **In-memory chat history using Redis** for fast and seamless conversations.
- **Azure AI Foundry integration** for deploying and managing OpenAI models.
- **Full Azure deployment** on **Azure Container Instances (ACI)** with a **Nginx-powered frontend** and a robust **backend API architecture**.
- **CI/CD Automation using GitHub Actions**, enabling automatic Docker image build, push, and Azure deployment.
- A **ready-to-use template** for anyone looking to build AI assistants, chatbots, or any AI-driven solutions on the Azure platform.

This template is ideal as a **starter project**, MVP, or full-scale production solution.

---

## 📌 Project Plan & Architecture

### Technologies & Services

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** PostgreSQL
- **In-Memory Cache:** Redis
- **LLM:** Azure AI Foundry
- **Containerization:** Docker
- **CI/CD Automation:** GitHub Actions
- **Hosting Containers:** Azure Container Instances (ACI)
- **Private Image Storage:** Docker Hub (Private Repository)
- **Optional (Production):** Azure PostgreSQL Database

---

## ⚡ Implementation Steps

### 🛠️ Step 1: Local Setup & Development

1. Set up Python & Flask backend
2. Configure PostgreSQL locally
3. Develop frontend (HTML, CSS, JS, Bootstrap)
4. Test APIs & frontend locally

### 🚀 Step 2: Containerize the Application

1. Create a Dockerfile for Flask, frontend, and PostgreSQL
2. Define services using `docker-compose.yml`
3. Run and test the application inside Docker

### 🔄 Step 3: Full Azure Deployment

1. Push code to GitHub (public repo)
2. Trigger GitHub Actions on push
3. Build Docker image locally
4. Push image to **Private Docker Hub Repository**
5. Deploy and replace running container in **Azure Container Instances (ACI)**
6. Integrate **Azure AI Foundry models** for AI chatbot functionality

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.11.0
- Docker 27.0.3
- Docker Compose v2.28.1
- Azure CLI installed


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




Step 1: Start Ubuntu
Since Ubuntu is stopped, we need to start it.

1.1 Open Ubuntu in WSL
In Command Prompt or PowerShell, run:

powershell
Copy
Edit
wsl -d Ubuntu
✅ This will start Ubuntu and open a Linux terminal.

Step 2: Install Redis in Ubuntu
Now that Ubuntu is running, let's install Redis inside it.

2.1 Update Package List
Run this command to update your system:

 
Edit
sudo apt update
2.2 Install Redis
Now, install Redis using:

 
Edit
sudo apt install redis -y
✅ This will install the latest Redis version.

Step 3: Start and Verify Redis
3.1 Start Redis Server
Run:

 
Edit
sudo service redis-server start
✅ This starts the Redis service.

3.2 Check Redis Status
To confirm Redis is running, use:

 
Edit
sudo service redis-server status
You should see something like:

arduino
Copy
Edit
● redis-server.service - Advanced key-value store
   Active: active (running) since ...
