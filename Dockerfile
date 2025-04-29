# Use the official lightweight Python image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (for PostgreSQL, build tools, etc)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy pyproject.toml and poetry.lock first to leverage Docker caching
COPY pyproject.toml poetry.lock* /app/

# Install dependencies via Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of your code
COPY . /app/

# Expose the port for ASGI/Daphne
EXPOSE 8000

# Default command to run Daphne server
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "django_portfolio.asgi:application"]
