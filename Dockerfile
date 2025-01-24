# Base Image
FROM continuumio/miniconda3:latest

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install Conda dependencies
RUN conda env create -f environment.yml

# Activate the Conda environment and set it as default
RUN echo "conda activate churn_env" >> ~/.bashrc
ENV PATH /opt/conda/envs/churn_env/bin:$PATH

# Install Ollama (example: adjust based on Ollama's installation method)
RUN curl -fsSL https://ollama.com/install | bash

# Set the entrypoint for running the script
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "churn_env", "python", "simulate_conversations.py"]
