# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:50:33 2021

@author: Bhuvi
"""

from kafka import KafkaConsumer

def multiconsume_pizza_messages():
    # consume latest messages and auto-commit offsets
    consumer = KafkaConsumer('new-pizza-orders',
                         #group_id='pizza-orders',
                         bootstrap_servers=['localhost:9099'],
                         #auto_offset_reset='earliest',
                         auto_offset_reset='latest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=1000)
    # Using multiple consumers in parallel
    consumer1 = KafkaConsumer('new-pizza-orders-0',
                         #group_id='pizza-orders',
                         bootstrap_servers=['localhost:9099'],
                         auto_offset_reset='latest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=1000)
    consumer2 = KafkaConsumer('new-pizza-orders-1',
                         #group_id='pizza-orders',
                         bootstrap_servers=['localhost:9099'],
                         auto_offset_reset='latest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=1000)
    keep_sending: bool = True
    try:
        while keep_sending:

            for message in consumer:

                print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
            
            for message1 in consumer1:

                print ("%s:%d:%d: key=%s value=%s" % (message1.topic, message1.partition,
                                          message1.offset, message1.key,
                                          message1.value))
                
            for message2 in consumer2:

                print ("%s:%d:%d: key=%s value=%s" % (message2.topic, message2.partition,
                                          message2.offset, message2.key,
                                          message2.value))
    

        
   
    except KeyboardInterrupt:
        print("Shutdown signal received. Closing consumer...")
        consumer.close(timeout=5)
        print("Consumer has been closed.")
