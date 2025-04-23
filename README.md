# FastAPI Docker Application

A containerized FastAPI application that provides a simple HTTP endpoint. This guide will walk you through every step of setting up and running the application.

## Detailed Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
1. **Docker**
   - For Mac: Install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - For Windows: Install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - For Linux: Follow the [Docker Engine installation guide](https://docs.docker.com/engine/install/)
   - Verify installation: `docker --version`

2. **Python 3.11** (if running locally)
   - Download from [Python's official website](https://www.python.org/downloads/)
   - Verify installation: `python --version`

### System Requirements
- Minimum 4GB RAM
- 10GB free disk space
- Internet connection for pulling Docker images and installing dependencies

## Project Structure Explained

```plaintext
.
├── main.py             # Contains the FastAPI application code and endpoints
├── Dockerfile          # Instructions for building the Docker container
└── requirements.txt    # Lists Python package dependencies (FastAPI and Uvicorn)
```

## Detailed Setup Instructions

### Option 1: Running with Docker (Recommended)

1. **Clone the Repository** (if applicable)
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Build the Docker Image**
   ```bash
   docker build -t fastapi-app .
   ```
   - The `-t` flag tags your image with the name "fastapi-app"
   - The `.` tells Docker to look for the Dockerfile in the current directory

3. **Run the Container**
   ```bash
   docker run -d -p 5000:5000 --name fastapi-container fastapi-app
   ```
   - `-d`: Runs the container in detached mode (background)
   - `-p 5000:5000`: Maps port 5000 on your host to port 5000 in the container
   - `--name fastapi-container`: Names your container for easy reference

4. **Verify the Container is Running**
   ```bash
   docker ps
   ```
   You should see "fastapi-container" in the list

5. **View Container Logs**
   ```bash
   docker logs fastapi-container
   ```

6. **Stop the Container**
   ```bash
   docker stop fastapi-container
   ```

7. **Remove the Container**
   ```bash
   docker rm fastapi-container
   ```

### Option 2: Running Locally

1. **Create and Activate Virtual Environment**

   For Mac/Linux:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   source venv/bin/activate
   ```

   For Windows:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   .\venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000 --reload
   ```
   - `--host 0.0.0.0`: Makes the server accessible from outside the host
   - `--port 5000`: Runs the server on port 5000
   - `--reload`: Enables auto-reload on code changes (development only)

## API Documentation

### Root Endpoint (`/`)
- **URL**: `http://localhost:5000/`
- **Method**: GET
- **Description**: Returns a welcome message
- **Response Format**:
  ```json
  {
    "message": "Hello from FastAPI!"
  }
  ```
- **Test with curl**:
  ```bash
  curl http://localhost:5000/
  ```

### Interactive API Documentation
FastAPI provides automatic interactive API documentation:
- Swagger UI: Visit `http://localhost:5000/docs`
- ReDoc: Visit `http://localhost:5000/redoc`

## Troubleshooting Guide

### Docker Issues

1. **Container Won't Start**
   ```bash
   # Check if port 5000 is already in use
   lsof -i :5000
   
   # Check container logs
   docker logs fastapi-container
   ```

2. **Permission Issues**
   ```bash
   # If you get permission errors on Linux
   sudo usermod -aG docker $USER
   # Log out and back in for changes to take effect
   ```

3. **Build Issues**
   ```bash
   # Clean up Docker system
   docker system prune -a
   # Rebuild with no cache
   docker build --no-cache -t fastapi-app .
   ```

### Local Development Issues

1. **Package Installation Failures**
   ```bash
   # Upgrade pip
   pip install --upgrade pip
   
   # Install with verbose output
   pip install -r requirements.txt -v
   ```

2. **Port Already in Use**
   ```bash
   # For Mac/Linux
   kill $(lsof -t -i:5000)
   
   # For Windows
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   ```

3. **Common Build Errors**
   - **CMake Missing Error**
     ```bash
     error: command 'cmake' failed: No such file or directory
     ```
     Solution:
     - For Mac: `brew install cmake`
     - For Ubuntu/Debian: `sudo apt-get install cmake`
     - For Windows: Download and install from [CMake's official website](https://cmake.org/download/)

   - **Wheel Build Failures**
     ```bash
     ERROR: Failed building wheel for [package-name]
     ```
     Solution:
     - Install build essentials:
       - For Mac: `xcode-select --install`
       - For Ubuntu/Debian: `sudo apt-get install build-essential`
       - For Windows: Install Visual Studio Build Tools
     - Try installing with: `pip install --no-binary :all: [package-name]`

## Development Guidelines

### Adding New Dependencies
1. Add to `requirements.txt`
2. Rebuild Docker image:
   ```bash
   docker build -t fastapi-app .
   ```

### Code Style
- Follow PEP 8 guidelines
- Use type hints for function parameters
- Document new endpoints using docstrings

## Monitoring and Maintenance

### Docker Container Health Check
```bash
# Check container health
docker inspect fastapi-container

# View container resource usage
docker stats fastapi-container
```

### Application Logs
```bash
# Docker logs
docker logs -f fastapi-container

# Local logs (when running with uvicorn)
# Logs will appear in the terminal
```

## Security Considerations

1. **Docker Security**
   - Using slim base image to minimize attack surface
   - No sensitive data in Docker image
   - Non-root user recommended for production

2. **API Security**
   - CORS not configured (add if needed)
   - No authentication required (add if needed)
   - Running on all interfaces (0.0.0.0)

## Version Information
- Python: 3.11
- FastAPI: Latest stable
- Uvicorn: Latest stable
- Docker: Compatible with Docker Engine 20.10+
