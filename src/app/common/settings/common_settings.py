from pydantic import BaseSettings, Field

class CommonSettings(BaseSettings):
    environment: str = Field(default='homolog')
    http_port: int
    event_sender: str

    class Config:
        env_file_encoding = 'utf-8'
        fields = {
            'event_sender': {
                'env': 'event_sender'
            },
            'environment': {
                'env': 'environment'
            },
            'http_port': {
                'env': 'http_port'
            }
        }
