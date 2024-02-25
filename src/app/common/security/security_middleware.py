from fastapi_keycloak_middleware import KeycloakConfiguration, KeycloakMiddleware

from src.app.common.utils.logger import logger
from src.app.common.settings.common_settings import CommonSettings

class SecurityMiddleware:

    def __init__(self):
        self.settings = CommonSettings()
        self.config = KeycloakConfiguration(
            url =           self.settings.keycloak_url,
            realm =         self.settings.keycloak_realm,
            client_id =     self.settings.keycloak_client_id,
            client_secret = self.settings.keycloak_client_secret,
            # reject_on_missing_claim=False, # Control behaviour when claims are missing,
        )

        self.excluded_routes = [
            # "/",
            # "/status",
            # "/docs",
            # "/openapi.json",
            # "/redoc",
        ]
        self.middleware = KeycloakMiddleware
        logger.info(f'Create SecurityMiddleware with URI {self.settings.keycloak_url}')