import pika
import os

host="10.44.197.243"
port="31500"
credentials = pika.PlainCredentials('user','nutanix/5u') #change cred for error in pod
parameters = pika.ConnectionParameters(host,port,'/',credentials)
while True:
  try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
  except pika.exceptions.ProbableAuthenticationError:
    print("failedauth error")

