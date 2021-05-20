import pika, json


params = pika.URLParameters('amqps://dhradflj:1gzwBw5slv45DEDYBcaN-77z51b8d1Mg@fly.rmq.cloudamqp.com/dhradflj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='localhost'))
    # channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
        body=json.dumps(body), properties=properties)