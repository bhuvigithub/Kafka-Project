# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:17:02 2021

@author: Bhuvi
"""

from kafka import KafkaProducer
from kafka.errors import KafkaError

def produce_messages():
    #Check with ClusterIP
    #producer = KafkaProducer(bootstrap_servers=['10.109.167.22:9092'],api_version=(0,22,1))
    #Check with NodePort
    producer = KafkaProducer(bootstrap_servers=['localhost:9095'])

    # Asynchronous data send
    data = producer.send('test-topic', b'Hola!')

    # Block for Synchronous data send
    try:
        record_metadata = data.get(timeout=10)
    except KafkaError as e: 
        print('Producer Error' + str(e))
        # Deciding what to do if produce request fails
        pass

    # Print assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)

    # produce key value messages
    producer.send('test-topic', key=b'food', value=b'pasta')

    # produce asynchronously simple message
    for _ in range(10):
        producer.send('test-topic', b'Hello World!')

    def on_send_success(record_metadata):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    def on_send_error(excp):
        print('Error exception', excp)
        # handle exception

    # asynchronous producer with callbacks
    producer.send('test-topic', b'Hello').add_callback(on_send_success).add_errback(on_send_error)

    # Wait until all async messages are sent
    producer.flush()
    producer.close()

    # configure multiple retries
    #producer = KafkaProducer(retries=5)
#produce_messages()