# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:17:21 2021

@author: Bhuvi
"""

from kafka import KafkaConsumer

def consume_messages():
    # consume latest messages and auto-commit offsets
    consumer = KafkaConsumer('test-topic',
                         group_id='test-group',
                         bootstrap_servers=['10.109.167.22:9092'],api_version=(0,22,1))
    for message in consumer:
    
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

#consume_messages()
# consume earliest available messages, but don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# StopIteration if no message received after 1sec
KafkaConsumer(consumer_timeout_ms=1000)

# Subscribe to the regex topic pattern
#consumer = KafkaConsumer()
#consumer.subscribe(pattern='^awesome.*')

# Using multiple consumers in parallel

#consumer1 = KafkaConsumer('test-topic',
 #                         group_id='test-group',
  #                        bootstrap_servers=['10.109.167.22:9091'],api_version=(0,22,1))
#consumer2 = KafkaConsumer('test-topic',
 #                         group_id='test-group',
  #                        bootstrap_servers=['10.109.167.22:9093'],api_version=(0,22,1))