# Use the official Python image with specific version suitable for Mac silicon
FROM python:3.9-slim

# Install wkhtmltopdf dependencies
RUN apt-get update && \
    apt-get install -y \
    wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run the application
CMD ["python", "main.py"]
