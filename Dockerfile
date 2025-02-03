
# Use an official Python runtime as a parent image
FROM python:3.1
1-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.11 \
        python3-pip \
        wget \
        tree \
        nano \
        llama.cpp \
        gcc \
        cmake \
        ccache \
        busybox \
        util-linux \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into
 the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
