FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project, including fastapi_crew
COPY . .

# Install the local package in development mode
# RUN pip install -e ./fastapi_crew  

# Use the main.py in the project root as the entry point
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]