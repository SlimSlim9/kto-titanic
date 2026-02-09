import os
import httpx
# TODO : importer la librairie facilitant la mise en place de server MCP
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from titanic.mcp_server.auth import token_manager

API_URL = os.getenv("TITANIC_API_URL", "http://titanic-api-service.slimzch-dev.svc.cluster.local:8080")

# TODO : Créer le server MCP avec le bon nom : "titanic-mcp-server"

# TODO : déclarer cette fonction en tant que tool
async def predict_survival(pclass: int, sex: str, sibsp: int, parch: int) -> str:
    """
    Prédit la survie d'un passager du Titanic.

    Args:
        pclass: Classe du billet (1, 2 ou 3)
        sex: Sexe ("male" ou "female")
        sibsp: Nombre de frères/sœurs/conjoints à bord
        parch: Nombre de parents/enfants à bord

    Returns:
        Prédiction de survie avec message et détails

    """
    # TODO : Implémenter l'appel http sécurisé avec oAuth2 vers l'API titanic
    return "Tool not implemented yet"

# TODO : A des fins de surveillances dans openshift, créer une custom route GET /health pour le server MCP

if __name__ == "__main__":
    # TODO : Démarrer le server web en local, sur le port 8080, en transport streamable-http
    print("toto")