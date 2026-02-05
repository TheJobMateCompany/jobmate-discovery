FROM python:3.10-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copie des requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du proto et du code
COPY proto ./proto
COPY . .

# Variable d'environnement pour que Python trouve les modules générés
ENV PYTHONPATH="${PYTHONPATH}:/app/proto/gen/python"
# Désactive le buffering pour voir les logs en temps réel
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]