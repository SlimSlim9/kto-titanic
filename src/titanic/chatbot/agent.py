import os
import asyncio
from typing import Any

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import SecretStr
# TODO : Importer le client MCP depuis la librairie facilitant les échanges MCP

# TODO : Définir le système Prompt

class ChatbotAgent:
    def __init__(self) -> None:
        mcp_server_host: str = os.getenv(
            "MCP_SERVER_HOST", "http://titanic-mcp-server.slimzch-dev.svc.cluster.local:8000"
        )
        # TODO : Mettre en place dans un attribut de classe la configuration du client MCP en déclarant les servers mcp cibles
        # TODO : Mettre en place dans un attribut de classe l'abstraction du LLM de Langchain en tant que ChatOpenAI
        # TODO : Faites en sorte que le mot de passe de l'API soit sécurisé avec pydantic SecretStr

    async def chat_async(self, message: str) -> str:
        """Chat async utilisant l'adaptateur MCP Langchain officiel."""
        # TODO : Créer le client MCP avec la configuration définie dans le constructeur
        # TODO : Récupérer les outils disponibles depuis le client MCP
        # TODO : Lier les outils au LLM pour obtenir un LLM capable d'utiliser les outils
        # TODO : Construire les messages avec le system prompt et le message utilisateur
        # TODO : Invoquer le LLM avec les messages construits
        # TODO : Vérifier si une tool a été appelée dans la réponse
        # TODO : Retourner le résultat du tool si c'est la réponse du llm, sinon, sa réponse générée.
        return ""

    def chat(self, message: str) -> str:
        return asyncio.run(self.chat_async(message))
