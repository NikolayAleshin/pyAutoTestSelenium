# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Chromium, ChromeDriver, curl, and other dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    chromium \
    chromium-driver \
    curl \
    && apt-get clean

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make ports available to the world outside this container
EXPOSE 5050
EXPOSE 5051

# Define environment variable for Allure results
ENV ALLURE_RESULTS=/app/allure-results

# Set environment variables (if needed)
ENV PYTHONUNBUFFERED=1

# Entry point for the tests and report generation
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["pytest --alluredir=/app/allure-results && curl -X GET http://allure:5050/generate-report && sleep 10"]
