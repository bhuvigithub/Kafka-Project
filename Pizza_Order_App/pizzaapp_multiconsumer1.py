import time
import argparse
#from multiconsumer import multiconsume_pizza_messages
from testconsumer1 import multiconsume_pizza_messages
from kafka.admin import KafkaAdminClient

if __name__ == "__main__":
    try:
        kafka_admin_client: KafkaAdminClient = KafkaAdminClient(
        bootstrap_servers='my-cluster-metrics-kafka-external-bootstrap:9099'
        )
        while True:
            multiconsume_pizza_messages(kafka_admin_client)
    except KeyboardInterrupt:
         print("Shutdown signal received. Closing consumer...")
         consumer.close(timeout=5)
         print("Consumer has been closed.")
