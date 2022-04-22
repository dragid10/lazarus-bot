FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8

RUN apt-get update
RUN apt-get install -y \
  git \
  zsh \
  python3-venv  \
  openjdk-11-jdk \
  build-essential \
  zlib1g-dev \
  libncurses5-dev \
  libgdbm-dev \
  libnss3-dev \
  libssl-dev \
  libsqlite3-dev \
  libreadline-dev \
  libffi-dev curl \
  libbz2-de \
  python3.9 \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64