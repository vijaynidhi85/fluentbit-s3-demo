import pika
host="10.44.197.243"
port="31510"
credentials = pika.PlainCredentials('user','nutanix/4u')
parameters = pika.ConnectionParameters(host,port,'/',credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
channel.start_consuming()

