import os
from collections.abc import Callable
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from jwt import PyJWKClient
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, InvalidAudienceError

# On définit le schéma de sécurité (Bearer Token)
security = HTTPBearer()

def verify_token(required_scope: str) -> Callable:
    """Create a token validator with a specific required scope using Auth0 JWKS."""

    async def _verify(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
        token = credentials.credentials

        # Récupération des variables d'environnement (configurées dans GitHub/OpenShift)
        auth0_domain = os.getenv("OAUTH2_DOMAIN")
        jwt_audience = os.getenv("OAUTH2_JWT_AUDIENCE", "titanic-api")

        # Si le domaine n'est pas configuré (test local), on laisse passer pour ne pas bloquer
        if not auth0_domain:
            return token

        try:
            # Récupération des clés publiques d'Auth0 pour vérifier la signature du JWT
            jwks_url = f"https://{auth0_domain}/.well-known/jwks.json"
            jwks_client = PyJWKClient(jwks_url)
            signing_key = jwks_client.get_signing_key_from_jwt(token)

            # Décodage et vérification du token
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=jwt_audience,
                issuer=f"https://{auth0_domain}/",
            )

            # Vérification des permissions (scopes)
            token_scopes = payload.get("scope", "")
            if isinstance(token_scopes, str):
                token_scopes = token_scopes.split()

            if required_scope and required_scope not in token_scopes:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Insufficient permissions. Required scope: {required_scope}",
                    headers={"WWW-Authenticate": f'Bearer scope="{required_scope}"'},
                )

            return token

        except ExpiredSignatureError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            ) from e
        except (InvalidAudienceError, InvalidTokenError) as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid token: {e!s}",
                headers={"WWW-Authenticate": "Bearer"},
            ) from e

    return _verify