FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

COPY weapons.txt ./weapons.txt

CMD ["python", "-m", "app.main"]