#!/bin/bash

# Start PostgreSQL service
service postgresql start

# Wait until PostgreSQL is ready
until pg_isready -U postgres; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

# 🔥 Set the PostgreSQL password manually
su - postgres -c "psql -c \"ALTER USER postgres WITH PASSWORD 'admin';\""

# Create database if it does not exist
su - postgres -c "psql -tc \"SELECT 1 FROM pg_database WHERE datname = 'mydb';\"" | grep -q 1 || \
    su - postgres -c "psql -c \"CREATE DATABASE mydb;\""

# Run database initialization script if it exists
if [ -f "/docker-entrypoint-initdb.d/init.sql" ]; then
  su - postgres -c "psql -d mydb -f /docker-entrypoint-initdb.d/init.sql"
  echo "Database initialized successfully."
else
  echo "Error: /docker-entrypoint-initdb.d/init.sql not found!"
fi

# Start Gunicorn for the Flask backend
echo "Starting Flask app with Gunicorn..."
gunicorn --bind 0.0.0.0:5000 --workers 4 backend.app:app &>> /var/log/flask.log &
# gunicorn --workers 4 --timeout 120 --bind 0.0.0.0:5000 backend.app:app

# Serve frontend using Python's HTTP server
cd frontend && python -m http.server 80 &>> /var/log/frontend.log &

# Keep the container running
tail -f /var/log/flask.log /var/log/frontend.log
