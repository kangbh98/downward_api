FROM python:3.8-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app
COPY app.py app.py

RUN pip install flask  # Flask 패키지 직접 설치

CMD ["python", "app.py"]
