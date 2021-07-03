# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:50:33 2021

@author: Bhuvi
"""

from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient
import os
#from decouple import config

def multiconsume_pizza_messages(kafka_admin_client):
    #kafka_admin_client: KafkaAdminClient = KafkaAdminClient(
     #   bootstrap_servers='10.105.85.14:9099'
    #)

    broker_topics = kafka_admin_client.list_topics()
    print(broker_topics)
    no_of_topics = int(os.getenv('NO_OF_TOPICS'))
    base_topic_name = os.getenv('TOPIC_NAME')
    #no_of_topics = int(config('NO_OF_TOPICS'))
    #base_topic_name = config('TOPIC_NAME')
    
    for i in range(1,no_of_topics+1):
        Exists=False
        name=f"{base_topic_name}-{i}"
        for j in (broker_topics):
           # if j.topics.get(j.topic_name)==name:
            if j == name:
                Exists=True
                break
        if Exists:
            consumer = KafkaConsumer(f"{name}",
                         group_id='pizza-order',
                         bootstrap_servers=['10.105.85.14:9099'],
                         #auto_offset_reset='earliest',
                         auto_offset_reset='latest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=1000)
    # consume latest messages and auto-commit offsets
   
            #keep_sending: bool = True
        #try:
                #while keep_sending:
            consumer.poll()
        
            for message in consumer:
        
                 print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))
                    
                    
            consumer.commit()
        
                
           
           # except KeyboardInterrupt:
            #    print("Shutdown signal received. Closing consumer...")
             #   consumer.close(timeout=5)
             #   print("Consumer has been closed.")
       

