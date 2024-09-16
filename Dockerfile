# syntax=docker/dockerfile:1.4

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# You may copy more files like csv, images, data
COPY app.py .


EXPOSE 8080

# Create a non-root user and switch to it
RUN useradd -m app_user
USER app_user

CMD [ "marimo", "run", "app.py", "--host", "0.0.0.0", "-p", "8080" ]
