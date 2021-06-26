# -*- coding: utf-8 -*-
"""
Created on Thu June 24 11:42:51 2021

@author: Bhuvi
"""

import time
import random
#import os
from faker import Faker
import json
from kafka import KafkaProducer
from producer_pizza import PizzaSupplier
from decouple import config
from topiccreation import execute_topic_creation
#import argsparse
import logging
from kafka.errors import NoBrokersAvailable
#from unbalanced import send_unbalanced_message_to_kafka
from random import randrange

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
def produce_pizza_messages(topic_name='new-pizza-orders',
                 no_of_messages=-1,
                 max_waiting_time_in_sec=5):
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9099'],
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
    )
    if no_of_messages <= 0:
        no_of_messages = float('inf')
    i = 0
    try:

        while i < no_of_messages:
            message, key = gen_pizza_order(i)

            print("Sending: {}".format(message))
             # sending the message to Kafka
            producer.send(topic_name,
                         key=key,
                         value=message)
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
    tn = config('TOPIC_NAME')
    nom = config('NO_OF_MESSAGES')
    mwt = config('MAX_WAIT_TIME')
    ntop = config('NO_OF_TOPICS')
    nptp = config('PARTITIONS_PER_TOPIC')
    nrpp = config('REPLICAS_PER_PARTITIONS')
    
    topic_list = topics_creation(base_topic_name=tn, no_of_topics=int(ntop), 
                    per_topic_partition=int(nptp), 
                    no_of_repicas_per_partition=int(nrpp))
    while True:
        rnd_index = randrange(len(topic_list))
        topic = topic_list[rnd_index]
       # for topic in topic_list:
        produce_pizza_messages(topic_name=topic,
         no_of_messages=int(nom),
         max_waiting_time_in_sec=float(mwt)
         )
        print(nom)

if __name__ == "__main__":
    main()
    
  
