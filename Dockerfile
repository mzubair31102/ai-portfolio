# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql postgresql-contrib \
    nginx

# Ensure database folder is accessible
RUN mkdir -p /var/lib/postgresql/data && chown -R postgres:postgres /var/lib/postgresql

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/sites-available/default

# Copy database initialization script
COPY database/init.sql /docker-entrypoint-initdb.d/init.sql
ENV FLASK_ENV=development

# Expose necessary ports
EXPOSE 80 5000 5432

# Set entrypoint
ENTRYPOINT ["bash", "entrypoint.sh"]
