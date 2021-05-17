# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:17:21 2021

@author: Bhuvi
"""

from kafka import KafkaConsumer

def consume_messages():
    # consume latest messages and auto-commit offsets
    consumer = KafkaConsumer('test-topic',
                         #group_id='test-group',
                         #ClusterIP check
                         #bootstrap_servers=['10.109.167.22:9092'],api_version=(0,22,1))
                         #Nodeport Check
                         bootstrap_servers=['localhost:9095'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=1000)


    for message in consumer:
    
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))


# Subscribe to the regex topic pattern
#consumer = KafkaConsumer()
#consumer.subscribe(pattern='^awesome.*')

# Using multiple consumers in parallel

#consumer1 = KafkaConsumer('test-topic',
 #                         group_id='test-group',
  #                        bootstrap_servers=['localhost:9095'])
#consumer2 = KafkaConsumer('test-topic',
 #                         group_id='test-group',
  #                        bootstrap_servers=['localhost:9095'])