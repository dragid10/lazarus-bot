FROM python:3.9.9-slim

# Python env flags
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ENV PYTHONFAULTHANDLER=1

# Poetry env flags
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV POETRY_NO_INTERACTION=1

# OS Update / Upgrade packages
RUN apt update \
    && apt upgrade -y \
    && apt autoremove -y \
    && apt clean

# Install Poetry
RUN pip install Poetry

# Change workdir
WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy modules to cache them in docker layer
COPY . /app/
ENV PYTHONPATH /app/*
CMD ["poetry", "run", "python", "-m", "main"]


