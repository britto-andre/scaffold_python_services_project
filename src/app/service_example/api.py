from fastapi import FastAPI, HTTPException, status, Body
from src.app.common.utils.logger import logger
from src.app.service_example.service.example_service import ExampleService
from src.app.service_example.entity.example import Example

import pika

app = FastAPI()

@app.get("/")
async def home():
    logger.debug('access home.')
    obj = Example(id=1234, name='Teste Name')
    service = ExampleService()
    service.create(obj, 'api', 'queue_test')
    return obj

@app.get("/test")
async def test():

    params = pika.URLParameters('amqp://guest:guest@localhost/%2f')
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)

    channel = connection.channel() # start a channel
    channel.queue_declare(queue='example_created') # Declare a queue
    
    # send a message    
    channel.basic_publish(exchange='example_exchange', routing_key='', body=b'Test message Britto.')
    connection.close()

    return 'Ok'


@app.delete("/example/{id}", response_description="Delete a example")
async def delete_example(id: str):
    # delete_result = await student_collection.delete_one({"_id": ObjectId(id)})

    # if delete_result.deleted_count == 1:
    #     return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Example {id} not found")


@app.post(
    "/example/",
    response_description="Add new example",
    response_model=Example,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_student(obj: Example = Body(...)):
    """
    Insert a new student record.

    A unique `id` will be created and provided in the response.
    """
    logger.info(obj)
    # new_student = await student_collection.insert_one(
    #     student.model_dump(by_alias=True, exclude=["id"])
    # )
    # created_student = await student_collection.find_one(
    #     {"_id": new_student.inserted_id}
    # )
    return obj