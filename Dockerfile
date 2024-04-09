FROM python:3.9-alpine3.13

LABEL maintainer='IreneSarah'

ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache gcc musl-dev python3-dev

# Install Flake8 and its dependencies as root
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install flake8

# Set up the application directory
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY . /app

WORKDIR /app
EXPOSE 8000

# Set up user
ARG DEV=false
RUN /py/bin/pip install -r /tmp/requirements.txt && \
    adduser --disabled-password --no-create-home django-user && \
    if [ $DEV = "true" ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    chown -R django-user /py && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"

USER django-user
