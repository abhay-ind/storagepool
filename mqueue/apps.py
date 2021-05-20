from django.apps import AppConfig
import multiprocessing,threading
from .consumer import consume as main

class MqueueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqueue'

    # print("TEST")

    p_consumer = threading.Thread(target=main)
    p_consumer.setDaemon(True)
    p_consumer.start()
    # p_consumer.join()