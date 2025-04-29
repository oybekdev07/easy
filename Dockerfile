FROM python:3.11-slim

# PortAudio kutubxonasini o‘rnatamiz
RUN apt-get update && apt-get install -y portaudio19-dev

# Ishchi katalogni o‘rnatamiz
WORKDIR /app
COPY . .

# Python kutubxonalarni o‘rnatamiz
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Dastur ishga tushadi
CMD ["python", "main.py"]
