# FastApi + nuitka + docker for linux

Create executable for FastApi using docker. (linux executable).
This project demonstrates how to containerize a FastAPI application using a lightweight Python image and Nuitka for creating standalone binaries on linux.

## Prerequisites

- Docker installed on your system
- A `main.py` file containing your FastAPI application
- A `requirements.txt` file listing the dependencies for your application

### Build docker image for standalone binary

```bash
docker build -t fastapi-nuitka-app .
```

### Create temporary container

```bash
docker create --name temp-container fastapi-nuitka-app
```

### Copy generated standalone binary main.bin to local directory

```bash
docker cp <container_id>:/app/main.bin /path/to/local/directory
```

- if you dont have linux to run binary then you can use [this](https://github.com/winnee0solta/fast_api_nuitka_docker/blob/main/linux/test_binary/README.md) to test binary.

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
