from pydantic import Field
from pydantic_settings import BaseSettings

class CommonSettings(BaseSettings):
    environment: str = Field(default='homolog')
    event_sender: str = Field(default='sender_unknow')
    event_queue_store: str = Field(default='application_event_store')
    amqp_uri: str = Field(default='amqp://guest:guest@localhost/%2f')
    mongo_uri: str = Field(default='mongodb://localhost:27017/')
    keycloak_url: str = Field(default='')
    keycloak_realm: str = Field(default='')
    keycloak_client_id: str = Field(default='')
    keycloak_client_secret: str = Field(default='')

    class Config:
        env_file_encoding = 'utf-8'
        env_file = '.env'
