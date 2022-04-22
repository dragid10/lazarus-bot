FROM python:3.9.12-bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8

RUN apt-get update
RUN apt-get install -y \
  git \
  zsh \
  python3-venv  \
    && rm -rf /var/lib/apt/lists/*