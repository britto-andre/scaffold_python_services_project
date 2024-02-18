from src.app.common.utils.logger import logger
from src.app.common.event.event import Event
from src.app.common.settings.common_settings import CommonSettings

from pymongo import MongoClient

class DefaultRepository:

    def __init__(self):
        self.settings = CommonSettings()
        logger.info(f'Create DefaultRepository with URI {self.settings.mongo_uri}')

    def client(self) -> MongoClient:
        return MongoClient(host=self.settings.mongo_uri)