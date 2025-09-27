# Start with a lightweight image that has Python and pip installed
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app
COPY . /app/

# Install system dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose the port that the app runs on
EXPOSE 8000