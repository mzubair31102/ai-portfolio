# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Ensure database folder is accessible
RUN mkdir -p /var/lib/postgresql/data && chown -R postgres:postgres /var/lib/postgresql

# Copy database initialization script
COPY database/init.sql /docker-entrypoint-initdb.d/init.sql

# Set environment variables
ENV FLASK_APP=backend/app.py
ENV FLASK_ENV=development
ENV POSTGRES_DB=mydb
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=admin

# Expose necessary ports
EXPOSE 80 5000 5432

# Set entrypoint
ENTRYPOINT ["bash", "entrypoint.sh"]
