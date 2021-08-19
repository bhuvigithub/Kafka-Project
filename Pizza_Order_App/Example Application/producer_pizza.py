# -*- coding: utf-8 -*-
"""
Created on Tue May 17 00:37:19 2021

@author: Bhubanesh Mishra
"""
# logic inspired from this repo - https://github.com/aiven/kafka-python-fake-data-producer
#changes made as per the project requirement
import random
from faker.providers import BaseProvider

# Adding a PizzaProvider with 3 methods:
#   * pizza_name to retrieve the name of the basic pizza,
#   * pizza_topping for additional toppings
#   * pizza_shop to retrieve one of the shops available
class PizzaSupplier(BaseProvider):
    def pizza_names(self):
        correct_pizza_names = [
            'Margherita',
            'Napolitana',
            'Vegano',
            'Chicago-Style',
            'Romana',
            'Peperoni',
            'Hawaiin',
            'Quatrro Parma',
            'Di Mexicano',
            'Calazone'
        ]
        return correct_pizza_names[random.randint(0, len(correct_pizza_names)-1)]

    def pizza_toppings(self):
        extra_pizza_toppings = [
            'plum tomato',
            'mozzarella',
            'sweet corn',
            'salami',
            'peppers',
            'ham',
            'olives',
            'anchovies',
            'artichokes',
            'mushrooms',
            'basil',
            'chicken',
            'onion',
            'pineapple',
            'chillies',
            'goat cheese',
            'spinach',
            'pine nuts',
            'capers',
            'prawns',
            'vegan cheese'
        ]
        return extra_pizza_toppings[random.randint(0, len(extra_pizza_toppings)-1)]

    def pizza_outlets(self):
        pizza_outlets = [
            'Pizza Express',
            'Jamie Italian Pizza',
            'Pizzeria Italia',
            'Zizi Pizza',
            'Fransesca Pizza',
            'Pizza di Napoli'
        ]
        return pizza_outlets[random.randint(0, len(pizza_outlets)-1)]