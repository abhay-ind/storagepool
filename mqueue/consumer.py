import mysql.connector
from mysql.connector import Error
import hashlib
from hmac import compare_digest
import os
import datetime
import pika, json


def consume():
    credentials = pika.credentials.PlainCredentials(username='quzulkbp', password='pEJ3Ssn5ev6Hs32zQYyEqb04AC6xCp98')
    parameters = pika.ConnectionParameters(
        host='puffin.rmq2.cloudamqp.com',
        virtual_host='quzulkbp',
        credentials=credentials,
        heartbeat=600,
        blocked_connection_timeout=300
    )
    connection = pika.BlockingConnection(parameters)
    
    # params = pika.URLParameters('amqps://quzulkbp:pEJ3Ssn5ev6Hs32zQYyEqb04AC6xCp98@puffin.rmq2.cloudamqp.com/quzulkbp')
    # connection = pika.BlockingConnection(params)

    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()
    channel.queue_declare(queue='main')

    def sha1sum(filepath):
        sha1_ob = hashlib.sha1()

        with open(filepath, "rb") as f:

            byte = f.read()
            while(byte):
                sha1_ob.update(byte)
                byte = f.read(1)

        return sha1_ob.hexdigest()

    print(os.listdir())
    def callback(ch, method, properties, body):
        data = json.loads(body)
        # print(data)

        
        pk = data['id']
        loc = data['filepath'][1:]

        hash = sha1sum(loc)
        fSize = os.path.getsize(loc)
        data['sha1sum'] = hash
        print(data)

        try:
            print("working")
            conn = mysql.connector.connect(host='localhost',
                                        port='3306',
                                        database='filez',
                                        user='root',
                                        password='Oxyfy@2021',
                                        )
        except Error as e:
            print("Error!!! ", e)
        print("connected")

        cursor = conn.cursor(buffered=True)

        cursor.execute(f"SELECT * FROM filez.uploads_filemodel WHERE sha1sum = '{hash}';")

        row = cursor.fetchone()

        print(row)
        if(row != None):
            id,namefield,filepath,hash,fs,ts = row 
            if(id != pk):
                os.remove(loc)
                cursor.execute(f"UPDATE filez.uploads_filemodel SET sha1sum='{hash}', filepath='{filepath}', filesize={fSize}, timestamp='{datetime.datetime.now()}' WHERE id={pk}")
                conn.commit()
        else:
            cursor.execute(f"UPDATE filez.uploads_filemodel SET sha1sum='{hash}', filesize={fSize}, timestamp='{datetime.datetime.now()}' WHERE id={pk}")
            conn.commit()

        conn.close()

    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
    print('Started Consuming')
    channel.start_consuming()
    channel.close()



if __name__ == "__main__":
    consume()