# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql postgresql-contrib \
    nginx \
    redis-server

# Ensure database folder is accessible
RUN mkdir -p /var/lib/postgresql/data && chown -R postgres:postgres /var/lib/postgresql

# Install Python dependencies
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/sites-available/default

# Copy database initialization script
COPY database/init.sql /docker-entrypoint-initdb.d/init.sql

# Expose necessary ports
EXPOSE 80 5000 5432 6379

# Set environment variable for Flask development
ENV FLASK_ENV=development

# Copy all project files
COPY . /app

# Set entrypoint
ENTRYPOINT ["bash", "entrypoint.sh"]
