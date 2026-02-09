"""
Ce script permet d'inférer le model de machine learning et de le mettre à disposition
dans un Webservice. Il pourra donc être utilisé par notre chatbot par exemple,
ou directement par un front. Remplir ce script une fois l'entrainement du model fonctionne
"""

import os

# TODO : Importer les dépendances utiles au bon développement en Python (dataclass, enum, pandas)
# TODO : Importer les dépendances pour sérialiser / désérialiser le model

# TODO : Importer les dépendances fastAPI
# TODO : Importer les dépendances OTEL pour le monitoring

from titanic.api.auth import verify_token


JAEGER_ENDPOINT = os.getenv("JAEGER_ENDPOINT", "http://jaeger.slimzch-dev.svc.cluster.local:4318/v1/traces")

# TODO : Intégrer les configurations d'OTEL et instancier le tracer. Peut être fait plus tard si le cours
# sur l'observabilité n'est pas encore donné

# TODO : Instancier l'application FastAPI

# TODO : Ouvrir et charger en mémoire le pickle qui sérialise le model

# TODO : Créer les class et dataclass représentant la donnée qui sera transmise au Webservice pour l'inférence

# TODO : Créer Pclass (enum)
# TODO : Créer Sex (enum)
# TODO : Créer Passenger (attention, l'objet doit pouvoir être transmis en dictionnaire au model. Il faudra créer une méthode d'instance

# TODO : Faire en sorte que cette fonction soit exposée via une toute GET /health
def health() -> dict:
    return {"status": "OK"}

# TODO : Faire en sorte que cette fonction soit exposée via une route POST /infer
# TODO : Ajouter les paramètres de la fonction (peut se faire en deux fois avec la sécurisation via oAuth2)
def infer() -> list:
    # TODO : implémenter le corps de la fonction
    return [0]
