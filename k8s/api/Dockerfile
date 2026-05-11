FROM python:3.13-slim

WORKDIR /app

# On installe les outils de compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ÉTAPE CLÉ : On copie TOUT le projet d'abord
# Ça va copier src/, data/, et ton fameux requirements.txt peu importe où il est
COPY . .

# On cherche le fichier requirements.txt là où il se trouve
# On utilise 'find' pour être sûr de le trouver, ou on pointe le chemin relatif
# Si tu l'as mis dans src/, change la ligne suivante en : RUN pip install -r src/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app/src
EXPOSE 8080

CMD ["python", "src/titanic/api/main.py"]