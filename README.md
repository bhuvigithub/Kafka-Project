# Kafka-Project

This repository is being used to track the Project progress and store the developed code for reference and review.

Errors encountered till now while running the code:
Error on Producer:
ubuntu@ip-172-31-17-242:~$ python3 app.py
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    produce_messages()
  File "/home/ubuntu/producers.py", line 15, in produce_messages
    data = producer.send('test-topic', b'Hola!')
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/producer/kafka.py", line 576, in send
    self._wait_on_metadata(topic, self.config['max_block_ms'] / 1000.0)
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/producer/kafka.py", line 702, in _wait_on_metadata
    raise Errors.KafkaTimeoutError(
kafka.errors.KafkaTimeoutError: KafkaTimeoutError: Failed to update metadata after 60.0 secs.

Error on Consumer:
ubuntu@ip-172-31-17-242:~$ python3 app.py
Traceback (most recent call last):
  File "app.py", line 9, in <module>
    from consumers import consume_messages
  File "/home/ubuntu/consumers.py", line 23, in <module>
    KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/consumer/group.py", line 356, in __init__
    self._client = KafkaClient(metrics=self._metrics, **self.config)
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/client_async.py", line 244, in __init__
    self.config['api_version'] = self.check_version(timeout=check_timeout)
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/client_async.py", line 900, in check_version
    raise Errors.NoBrokersAvailable()
kafka.errors.NoBrokersAvailable: NoBrokersAvailable

Error on Producer without API:
Traceback (most recent call last):
  File "producers.py", line 11, in <module>
    producer = KafkaProducer(bootstrap_servers=['10.109.167.22:9093'])
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/producer/kafka.py", line 381, in __init__
    client = KafkaClient(metrics=self._metrics, metric_group_prefix='producer',
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/client_async.py", line 244, in __init__
    self.config['api_version'] = self.check_version(timeout=check_timeout)
  File "/home/ubuntu/.local/lib/python3.8/site-packages/kafka/client_async.py", line 927, in check_version
    raise Errors.NoBrokersAvailable()
kafka.errors.NoBrokersAvailable: NoBrokersAvailable
