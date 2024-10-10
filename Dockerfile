# Use the official Python image.
FROM python:3.11-slim

# Install necessary dependencies.
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    google-chrome-stable

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code.
COPY . .

# Expose the port your application will run on.
EXPOSE 10000

# Specify the command to run your FastAPI app.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
