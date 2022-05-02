FROM python:3.9.12-slim as base

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



# Change workdir
WORKDIR /app

# Copy deps file to workdir
COPY . /app/
ENV PYTHONPATH /app/*

# PROD TARGET
FROM base as prod
RUN echo "Prod build"
# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --preview\
    && /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry install --only default
RUN /root/.local/bin/poetry run python -m main -d redis

# TEST TARGET
FROM base as test
RUN echo "Test build"
# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --preview\
    && /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry install --with test
CMD /root/.local/bin/poetry run pytest

# DEV TARGET
FROM base as dev
RUN echo "Dev build"
# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --preview\
    && /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry install
CMD /root/.local/bin/poetry run python -m main -d memory