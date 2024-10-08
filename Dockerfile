FROM python:3.8-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app
COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip install -r requirements.txt

CMD ["python", "app.py"]