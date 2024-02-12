FROM python:3.11-slim

RUN apt-get update && apt-get -y install curl

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY templates templates
COPY main.py .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000" ]