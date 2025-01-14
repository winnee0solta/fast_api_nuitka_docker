** Testing the binary with ubuntu docker image**

## Prerequisites

- Docker installed on your system
- copy the binary to test folder in our case main.bin
- make sure to cd to test_binary folder

## Build and Run the Docker Container

### 1. Build the Image

Run the following command to build the Docker image:

```bash
docker build -t test_binary_linux .
```

### 2. Run the Container

Run the Docker container using the following command:

```bash
docker run -p 8000:8000 test_binary_linux
```

This maps port 8000 on the container to port 8000 on your host machine.

### 3. Access the Application

Visit `http://localhost:8000` in your browser or use a tool like `curl` to access your FastAPI application.

## Notes

- Ensure your `main.py` contains a properly defined FastAPI app.
- If you encounter any issues with the compiled binary, verify that all necessary imports are included.
- Adjust the exposed port and entrypoint as needed for your application.

## Cleanup

To remove unused Docker images and containers, run:

```bash
docker system prune
```

## License

This project is licensed under the MIT License. Feel free to use and modify the Dockerfile for your own projects.
