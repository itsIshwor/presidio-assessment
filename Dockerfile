# Base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 8080

# Run the Flask application
CMD ["python", "app.py"]
