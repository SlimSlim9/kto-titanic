FROM python:3.13-slim

# On définit le répertoire de travail dans le container
WORKDIR /app

# On installe les dépendances système si nécessaire (souvent utile pour les libs de ML)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# On copie le fichier des dépendances
COPY requirements.txt .

# On installe les bibliothèques Python
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout ton code source
# C'est ici que GitHub va copier ton dossier 'src' dans le container
COPY . .

# --- ÉTAPE CRUCIALE POUR TON PROJET ---
# Comme ton code fait "from titanic.api...", il faut que Python regarde dans le dossier 'src'
ENV PYTHONPATH=/app/src

# Port utilisé par OpenShift
EXPOSE 8080

# On lance l'API via ton fichier main.py
CMD ["python", "src/titanic/api/main.py"]