FROM python:3.13-slim

# Mettre en place les trois arguments transmis par la CI/CD (ou le script)
ARG MLFLOW_S3_ENDPOINT_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# Les mettre en variables d'environnement pour que MlFlow fonctionne correctement
ENV MLFLOW_S3_ENDPOINT_URL=$MLFLOW_S3_ENDPOINT_URL
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

# Ajouter les variables d'env techniques (pour le répertoire tmp et le refresh git)
# Ces variables évitent des crashs de permissions sur OpenShift
ENV GIT_PYTHON_REFRESH=quiet
ENV TMPDIR=/tmp
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

# Bien mettre en place le répertoire de travail
WORKDIR /app

# Installer uv (on utilise pip qui est déjà dans l'image python slim)
RUN pip install uv

# Copier les sources utiles
COPY . /app/

# Installer les dépendances et python avec uv
RUN uv sync --all-groups

# À ajouter avant la fin de ton Dockerfile
# Création de l'utilisateur non-root (obligatoire pour OpenShift)
# Et on lui donne la propriété du dossier /app pour qu'il puisse exécuter le code
RUN useradd -u 1001 mlflowuser && \
    chown -R 1001:1001 /app

USER 1001