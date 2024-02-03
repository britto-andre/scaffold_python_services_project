
# import pika



# @app.get("/test")
# async def test():

#     params = pika.URLParameters('amqp://guest:guest@localhost/%2f')
#     params.socket_timeout = 5

#     connection = pika.BlockingConnection(params)

#     channel = connection.channel() # start a channel
#     channel.queue_declare(queue='example_created') # Declare a queue
    
#     # send a message    
#     channel.basic_publish(exchange='example_exchange', routing_key='', body=b'Test message Britto.')
#     connection.close()

#     return 'Ok'
