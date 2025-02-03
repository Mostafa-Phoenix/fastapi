# Use an official Python runtime as a parent image
FROM python
:3.11-slim-bookworm

# Set the working directory to /app
WORKDIR /app

# Install system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        tree \
        nano \
        build-essential \
        cmake \
        ccache \
        busybox \
        util-linux \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install
 any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model download script
COPY models/deepseek/download.sh /app/models/deepseek/

# Make the script executable
RUN chmod +x /app/models/deepseek/download.sh

# Download the model
RUN /app/models/deepseek/download.sh

# Copy the rest of the application files into the container
COPY . /app

# Make the devserver executable
RUN chmod +x devserver.sh

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run devserver-prod.sh when the container launches
CMD ["./devserver.sh"]
