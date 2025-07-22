# Dockerfile for a vulnerable Python container image
FROM python:3.12-slim

# Copy a simple Python application (optional)
COPY app.py /app/app.py

# Set working directory
WORKDIR /app

# Command to run the application
CMD ["python", "app.py"]