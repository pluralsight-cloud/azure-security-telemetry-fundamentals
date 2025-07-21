# Dockerfile for a vulnerable Python container image
FROM python:3.10.12-slim

# Install outdated packages with known vulnerabilities
# Example: Install an older version of pip and a vulnerable package
RUN pip install pip==20.0.2
RUN pip install requests==2.25.1

# Copy a simple Python application (optional)
COPY app.py /app/app.py

# Set working directory
WORKDIR /app

# Command to run the application
CMD ["python", "app.py"]