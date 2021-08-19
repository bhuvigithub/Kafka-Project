# -*- coding: utf-8 -*-
"""
Created on Wed May 12 20:48:33 2021

@author: Bhubanesh Mishra
"""
import time
from producers import produce_messages
from consumers import consume_messages

if __name__ == "__main__":
    produce_messages()
    
    time.sleep(5)
    
    consume_messages()