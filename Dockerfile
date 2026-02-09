FROM python:3.11-slim

LABEL maintainer="devops-team"
LABEL description="Sample Flask application deployed via Azure DevOps pipeline"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=myflaskapp.app:app

WORKDIR /app

# Copy the built wheel file into the container
COPY dist/*.whl /app/

# Install the wheel package (includes Flask as a dependency)
RUN pip install --no-cache-dir /app/*.whl

# Expose the Flask default port
EXPOSE 5000

# Run the application using the console_scripts entry point
CMD ["myflaskapp"]
