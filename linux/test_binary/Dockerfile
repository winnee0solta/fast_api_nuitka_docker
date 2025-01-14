# Use a minimal base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Copy the binary into the container
COPY main.bin /app/main.bin

# Make the binary executable
RUN chmod +x /app/main.bin

EXPOSE 8000
# Set the entrypoint to the binary
ENTRYPOINT ["/app/main.bin"]
