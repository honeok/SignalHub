FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p instance

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV DB_TYPE=sqlite

EXPOSE 5000

CMD ["python", "app.py"] 