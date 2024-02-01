import pika, time

def pdf_process_function(msg):
  print(" Message processing")
  print(" [x] Received " + str(msg))

  time.sleep(5) # delays for 5 seconds
  print(" PDF processing finished")
  return

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
params = pika.URLParameters('amqp://guest:guest@localhost:5672/%2f')
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='example_created') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  print(f" Message processing: {ch} - {method} - {properties} - {body}")

  time.sleep(5) # delays for 5 seconds
  print("Message processed!")
#   pdf_process_function(body)

print('Starting...')
# set up subscription on the queue
channel.basic_consume('example_created', callback, auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()