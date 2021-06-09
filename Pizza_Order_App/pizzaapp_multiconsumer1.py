import time
import argparse
#from multiconsumer import multiconsume_pizza_messages
from testconsumer1 import multiconsume_pizza_messages

if __name__ == "__main__":
    try:
        while True:



            multiconsume_pizza_messages()
    except KeyboardInterrupt:
         print("Shutdown signal received. Closing consumer...")
         consumer.close(timeout=5)
         print("Consumer has been closed.")
