from pydantic import Field
from pydantic_settings import BaseSettings

class CommonSettings(BaseSettings):
    environment: str = Field(default='homolog')
    event_sender: str = Field(default='api_unknow')

    class Config:
        env_file_encoding = 'utf-8'
        fields = {
            'event_sender': {
                'env': 'event_sender'
            },
            'environment': {
                'env': 'environment'
            }
        }
