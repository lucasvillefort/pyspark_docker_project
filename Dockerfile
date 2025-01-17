# Use an official Spark base image
FROM bitnami/spark:latest

# Install numpy
RUN pip install numpy pandas pyspark spark notebook

# Set the working directory
WORKDIR /app

# Copy your application code to the container
COPY . /app