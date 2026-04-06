FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean

# Install requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Uncomment when deploying
COPY . .

# Expose gradio port
EXPOSE 8000 

CMD ["sh", "-c", "python src/main.py --host 0.0.0.0 --port 8000"]