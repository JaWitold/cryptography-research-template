# Use an official Python runtime as a parent image
FROM python:3.14-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock ./

# Project initialization
RUN poetry install --no-root --only main

# Set PYTHONPATH to include the project root
ENV PYTHONPATH="/app"

# Copy the rest of the application
COPY . .

# Install the project itself
RUN poetry install --no-root --only main

# Set the default command to run the benchmarks
CMD ["poetry", "run", "python", "benchmarks/benchmark_bls.py"]
