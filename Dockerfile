FROM python:3.11-slim

# Tizim kutubxonalarini o‘rnatamiz
RUN apt-get update && apt-get install -y portaudio19-dev

# Loyihani konteynerga ko‘chir
WORKDIR /app
COPY . .

# Python kutubxonalarni o‘rnat
RUN pip install -r requirements.txt

# Dasturni ishga tushir
CMD ["python", "main.py"]
