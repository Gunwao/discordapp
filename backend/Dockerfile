# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     python3-tk \
#     ffmpeg \
#     && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file and install dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 to be able to access Flask
EXPOSE 5000

# Define the command to run the Flask app in development mode
CMD ["flask", "run", "--host=0.0.0.0"]
