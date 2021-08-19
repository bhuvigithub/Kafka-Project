# -*- coding: utf-8 -*-
"""
Created on Wed May 19 02:54:51 2021

@author: Bhubanesh Mishra
"""

from kafka import KafkaConsumer

def consume_pizza_messages():
    # consume latest messages and auto-commit offsets
    consumer = KafkaConsumer('new-pizza-orders',
                         #group_id='pizza-orders',
                         bootstrap_servers=['localhost:9097'],
                         #auto_offset_reset='earliest',
                         auto_offset_reset='latest',
                         enable_auto_commit=True,
                         consumer_timeout_ms=1000)
    keep_sending: bool = True
    try:
        while keep_sending:

            for message in consumer:

                print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    except KeyboardInterrupt:
        print("Shutdown signal received. Closing consumer...")
        consumer.close(timeout=5)
        print("Consumer has been closed.")
