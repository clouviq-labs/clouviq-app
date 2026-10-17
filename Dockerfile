FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir flask==3.1.2
COPY app.py .
ARG APP_VERSION=dev
ENV APP_VERSION=$APP_VERSION PORT=8080
EXPOSE 8080
USER 1000
CMD ["python", "app.py"]
