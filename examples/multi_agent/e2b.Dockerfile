# You can use most Debian-based base images
FROM e2bdev/code-interpreter:latest

# Install dependencies and customize sandbox
RUN pip install git+https://github.com/huggingface/smolagents.git

# Add any other dependencies you might need
RUN pip install litellm>=1.55.10

# Copy the content of the folder with the code needed to run the agent
COPY . /app

# Set the working directory
WORKDIR /app