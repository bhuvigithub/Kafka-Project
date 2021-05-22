# -*- coding: utf-8 -*-
"""
Created on Tue May 18 01:41:23 2021

@author: Bhuvi
"""

import time
import random
import argparse
from faker import Faker
import json
from kafka import KafkaProducer
from producer_pizza import PizzaSupplier

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
        bootstrap_servers=['localhost:9097'],
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


# calling the produce_pizza_messages function that take 3 parameters as inputs
# Param-1 - topic-name
# Param-2 - no-of-messages 
# Param-3 - max-waiting-time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic-name', help="Topic Name in which the messages would be send", required=True)
    parser.add_argument('--no-of-messages', help="Number of messages to produce per script run where 0 is for unlimited messages", required=True)
    parser.add_argument('--max-waiting-time', help="Max waiting time between messages in seconds", required=True)
    args = parser.parse_args()
    prod_topic_name=args.topic_name
    produce_pizza_messages(topic_name=prod_topic_name,
                 no_of_messages=int(args.no_of_messages),
                 max_waiting_time_in_sec=float(args.max_waiting_time)
                 )
    print(args.no_of_messages)

if __name__ == "__main__":
    main()
    
  