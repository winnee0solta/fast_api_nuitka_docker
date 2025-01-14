# Use a lightweight Python image
FROM python:3.13-slim

# Install required system dependencies
RUN apt update && apt install -y \
    build-essential \
    patchelf \
    curl \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Compile the FastAPI app using Nuitka
RUN pip install --no-cache-dir nuitka
RUN python3 -m nuitka --standalone --onefile --follow-imports main.py
