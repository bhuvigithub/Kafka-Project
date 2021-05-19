# -*- coding: utf-8 -*-
"""
Created on Wed May 19 02:54:51 2021

@author: Bhuvi
"""

from kafka import KafkaConsumer

def consume_pizza_messages():
    # consume latest messages and auto-commit offsets
    consumer = KafkaConsumer('new-pizza-orders',
                         bootstrap_servers=['localhost:9095'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=1000)


    for message in consumer:
    
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))