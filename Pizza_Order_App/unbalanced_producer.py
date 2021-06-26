# -*- coding: utf-8 -*-
"""
Created on Thu June 24 11:42:51 2021

@author: Bhuvi
"""

import time
import random
import os
from faker import Faker
import json
from kafka import KafkaProducer
from producer_pizza import PizzaSupplier
#from decouple import config
from topiccreation import execute_topic_creation
from typing import List, Dict
import logging
from kafka.errors import NoBrokersAvailable
from partition import sorting_partitions_by_leader
from kafka.admin import KafkaAdminClient
from kafka.errors import KafkaTimeoutError

LOG: logging.Logger = logging.getLogger("kafka-topic-loader.topic")

MAX_PIZZAS_PER_ORDER = 15
MAX_EXTRA_TOPPINGS_PER_PIZZA = 8



# Creating a Faker instance and seeding to have the same results every time we execute the script
fake = Faker()
Faker.seed(4321)



# Adding the newly created PizzaSupplier to the Faker instance
fake.add_provider(PizzaSupplier)

# creating function to generate the pizza Order
def gen_pizza_order (ordercount):
    outlet = fake.pizza_outlets()
    # Each Order can have 1-15 pizzas in it
    pizzas = []
    for pizza in range(random.randint(1, MAX_PIZZAS_PER_ORDER)):
        # Each Pizza can have 0-8 extra toppings on it
        toppings = []
        for topping in range(random.randint(0, MAX_EXTRA_TOPPINGS_PER_PIZZA)):
            toppings.append(fake.pizza_toppings())
        pizzas.append({
            'pizzaName': fake.pizza_names(),
            'extraToppings': toppings
        })
    # Pizza order complete message composition
    message = {
        'Orderid': ordercount,
        'OutletName': outlet,
        'CustomerName': fake.unique.name(),
        'CustomerPhoneNo': fake.unique.phone_number(),
        'Address': fake.address(),
        'PizzaType': pizzas
    }
    key = {'outlet': outlet}
    return message, key


# function produce_msgs starts producing messages with Faker
def produce_unbalanced_pizza_message(topic_name='new-pizza-orders',
                 no_of_messages=-1,
                 max_waiting_time_in_sec=5):
    LOG.info("Create Kafka Admin Client")
    kafka_admin_client: KafkaAdminClient = KafkaAdminClient(
        bootstrap_servers='10.98.131.151:9099'
        )
    # Get the mapping from topic to node id for partitions with leader replicas on that node
    topicleadnode: Dict[str, Dict[int, List[int]]] = sorting_partitions_by_leader(kafka_admin_client)

    # Get list of all node ids in the cluster
    LOG.info("Get the existing Kafka node list")
    nodes: List[int] = [node.nodeId for node in kafka_admin_client._client.cluster.brokers()]
    
    producer = KafkaProducer(
        bootstrap_servers=['10.98.131.151:9099'],
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
    )
    if no_of_messages <= 0:
        no_of_messages = float('inf')
    LOG.info("Loading %d topics", len(topicleadnode.keys()))
    i = 0
    try:

        while i < no_of_messages:
            message, key = gen_pizza_order(i)
            
            topic: str
            node_partiton_leader: Dict[int, List[int]]

            for topic, node_partiton_leaders in topicleadnode.items():
                multiplier: int = 1
                partitions: List[int]
                for partitions in node_partiton_leaders.values():
                    # For each node cycle through the partitions whose leaders are on that node
                    partition: int
                    for partition in partitions:
                        # For each partition send a number of messages depending on how far down the node list we are
                        for _ in range(multiplier):
                            try:
                                #print("Sending: {}".format(message))
                                # sending unbalanced messages to Kafka
                                producer.send(topic_name,
                                             key=key,
                                             value=message, partition=partition)
                            except KafkaTimeoutError:
                                LOG.error("Unable to fetch metadata")
                    # Send more messages to the next node in the list
                    multiplier += 1
            # Sleeping time
            sleep_time = random.randint(0, max_waiting_time_in_sec * 10)/10
            print("Sleeping for-"+str(sleep_time)+'secs')
            time.sleep(sleep_time)

             # Force flushing of all messages
            if (i % 100) == 0:
                 producer.flush()
            i = i + 1
    except KeyboardInterrupt:
        print("Shutdown signal received. Closing producer...")
        producer.close(timeout=5)
        print("Producer has been closed.")
    finally:
        producer.flush()

def topics_creation(**kwargs) -> None:

    LOG.info("Running topic creation process...")

    try:
        return execute_topic_creation(
            kwargs['base_topic_name'],
            kwargs['no_of_topics'],
            kwargs['per_topic_partition'],
            kwargs['no_of_repicas_per_partition']
        )
    except NoBrokersAvailable:
        LOG.error("No brokers available")


# calling the produce_pizza_messages function that take 3 parameters as inputs
# Param-1 - topic-name
# Param-2 - no-of-messages 
# Param-3 - max-waiting-time

def main():
   # parser = argparse.ArgumentParser()
    #args = parser.parse_args()
    tn = os.getenv('TOPIC_NAME')
    nom = os.getenv('NO_OF_MESSAGES')
    mwt = os.getenv('MAX_WAIT_TIME')
    ntop = os.getenv('NO_OF_TOPICS')
    nptp = os.getenv('PARTITIONS_PER_TOPIC')
    nrpp = os.getenv('REPLICAS_PER_PARTITIONS')
    
    topic_list = topics_creation(base_topic_name=tn, no_of_topics=int(ntop), 
                    per_topic_partition=int(nptp), 
                    no_of_repicas_per_partition=int(nrpp))
    while True:
        
     for topic in topic_list:
        produce_unbalanced_pizza_message(topic_name=topic,
         no_of_messages=int(nom),
         max_waiting_time_in_sec=float(mwt)
         )
        #print(nom)

if __name__ == "__main__":
    main()
    
  
