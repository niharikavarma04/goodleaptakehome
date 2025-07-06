# slim python3 image
FROM python:3.10-slim

# Setting working directory inside the container
WORKDIR /app

# Copies the current directory contents into the container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir requests

# Command to run the script
CMD ["python3", "github_repo_summary.py"]
