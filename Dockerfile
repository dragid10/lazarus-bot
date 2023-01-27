FROM python:3.10-slim as base

# Python env flags
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ENV PYTHONFAULTHANDLER=1

# Poetry env flags
ENV POETRY_VIRTUALENVS_IN_PROJECT=false
ENV POETRY_NO_INTERACTION=1

# OS Update / Upgrade packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y curl \
    && apt-get autoremove -y \
    && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --preview

# Change workdir
WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml /app/
RUN /root/.local/bin/poetry config virtualenvs.create false
RUN /root/.local/bin/poetry install --only default

# Copy modules to cache them in docker layer
COPY . /app/
ENV PYTHONPATH /app/*

RUN echo "Prod build"
CMD ["/root/.local/bin/poetry", "run", "python", "-m", "main", "-d", "redis"]
