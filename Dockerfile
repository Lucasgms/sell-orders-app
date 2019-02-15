# Use an official Python runtime as a parent image
FROM python:3.7.2-slim

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev gcc

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
#CMD ./config/init.sh
