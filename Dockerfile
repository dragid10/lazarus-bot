FROM python:3.9.12-slim as base

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
RUN curl -sSL https://install.python-poetry.org | python3 - --preview

# Change workdir
WORKDIR /app

# Copy deps file to workdir
COPY . /app/
ENV PYTHONPATH /app/*
RUN poetry config virtualenvs.create false

# TEST TARGET
FROM base as test
RUN poetry install --with test
RUN ["poetry", "run", "pytest"]

# DEV TARGET
FROM base as dev
RUN poetry install
RUN ["poetry", "run", "python", "-m", "main", "-d", "memory"]

# PROD TARGET
FROM base as prod
RUN poetry install --only default
RUN ["poetry", "run", "python", "-m", "main", "-d", "redis"]