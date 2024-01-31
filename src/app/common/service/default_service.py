from src.app.common.utils.logger import logger
from src.app.common.event.event import Event

class DefaultService:

    def create(self, payload, sender, queue):
        logger.info(payload)
        logger.info(sender)
        logger.info(queue)


        event = Event(
            _id=1234, 
            event_name= 'Evento de teste',
            aggregate_id= 12,
            aggregate_type= 'teste',
            sender= sender,
            payload= payload
            )

        # To-do
        # persist event
        # publish event
        logger.info(event)