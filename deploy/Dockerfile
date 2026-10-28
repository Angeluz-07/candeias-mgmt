FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean

COPY deploy/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src


CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]