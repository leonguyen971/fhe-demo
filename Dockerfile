# Dockerfile

FROM python:3.10-slim
WORKDIR /app
COPY . .
CMD ["python", "encrypt.py"]
