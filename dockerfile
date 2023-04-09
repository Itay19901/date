# Use an official Python
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY .. /app

EXPOSE 8080

# Run the Python program when the container starts
CMD [ "python", "date_listener.py" ]