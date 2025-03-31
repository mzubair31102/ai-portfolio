#!/bin/bash

# # Start PostgreSQL service
# service postgresql start

# # Wait for PostgreSQL to be ready
# until pg_isready -U postgres; do
#   echo "Waiting for PostgreSQL..."
#   sleep 2
# done

# # Set PostgreSQL password manually
# su - postgres -c "psql -c \"ALTER USER postgres WITH PASSWORD 'admin';\""

# # Create database if not exists
# su - postgres -c "psql -tc \"SELECT 1 FROM pg_database WHERE datname = 'mydb';\"" | grep -q 1 || \
#     su - postgres -c "psql -c \"CREATE DATABASE mydb;\""

# # Run database initialization script if exists
# if [ -f "/docker-entrypoint-initdb.d/init.sql" ]; then
#   su - postgres -c "psql -d mydb -f /docker-entrypoint-initdb.d/init.sql"
#   echo "Database initialized successfully."
# else
#   echo "Error: /docker-entrypoint-initdb.d/init.sql not found!"
# fi

# # Start Gunicorn for Flask backend
# echo "Starting Flask app with Gunicorn..."
# gunicorn --bind 0.0.0.0:5000 --workers 4 backend.app:app &>> /var/log/flask.log &

# # Start Nginx for serving frontend
# echo "Starting Nginx..."
# nginx -g 'daemon off;'
# echo "Nginx started successfully."




# Dev container entrypoint script
# This script is used to set up the development environment for a Flask application
#!/bin/bash

# Start PostgreSQL service
service postgresql start

# Wait for PostgreSQL to be ready
until pg_isready -U postgres; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

# Set PostgreSQL password manually
su - postgres -c "psql -c \"ALTER USER postgres WITH PASSWORD 'admin';\""

# Create database if not exists
su - postgres -c "psql -tc \"SELECT 1 FROM pg_database WHERE datname = 'mydb';\"" | grep -q 1 || \
    su - postgres -c "psql -c \"CREATE DATABASE mydb;\""

# Run database initialization script if exists
if [ -f "/docker-entrypoint-initdb.d/init.sql" ]; then
  su - postgres -c "psql -d mydb -f /docker-entrypoint-initdb.d/init.sql"
  echo "Database initialized successfully."
else
  echo "Error: /docker-entrypoint-initdb.d/init.sql not found!"
fi

# Enable Live Reload for Flask App
echo "Starting Flask app in development mode with auto-reload..."
cd /app/backend
FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000 --reload &>> /var/log/flask.log &

# Start Nginx for serving frontend
echo "Starting Nginx..."
nginx -g 'daemon off;'
