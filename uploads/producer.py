import pika, json


params = pika.URLParameters('amqps://quzulkbp:pEJ3Ssn5ev6Hs32zQYyEqb04AC6xCp98@puffin.rmq2.cloudamqp.com/quzulkbp')

connection = pika.BlockingConnection(params)

channel = connection.channel()

    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='localhost'))
    # channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
        body=json.dumps(body), properties=properties)