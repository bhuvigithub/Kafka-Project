FROM python:3

ADD producer_pizza.py /

ADD consumer_pizza.py /

ADD pizzaapp.py /

ADD envconfig.py /

ADD pizzaapp_consumer.py /

ADD multi_topic_producer1.py /

ADD topiccreation.py /

ADD multiconsumer.py /

ADD testconsumer1.py /

ADD pizzaapp_multiconsumer1.py /

ADD unbalanced_producer.py /

ADD unbalanced_test_producer.py /

ADD partition.py /

ARG KAFKA_TOPIC_NAME=new-pizza-orders

ARG KAFKA_NO_OF_MESSAGES=10

ARG KAFKA_MAX_WAIT_TIME=1

ARG KAFKA_NO_OF_TOPICS=3

ARG KAFKA_PARTITIONS_PER_TOPIC=3

ARG KAFKA_REPLICAS_PER_PARTITIONS=3

ENV TOPIC_NAME=$KAFKA_TOPIC_NAME

ENV NO_OF_MESSAGES=$KAFKA_NO_OF_MESSAGES

ENV MAX_WAIT_TIME=$KAFKA_MAX_WAIT_TIME

ENV NO_OF_TOPICS=$KAFKA_NO_OF_TOPICS

ENV PARTITIONS_PER_TOPIC=$KAFKA_PARTITIONS_PER_TOPIC

ENV REPLICAS_PER_PARTITIONS=$KAFKA_REPLICAS_PER_PARTITIONS

RUN pip install kafka

RUN pip install argparse 

RUN pip install kafka-python

RUN pip install faker

RUN pip install python-decouple

CMD [ "unbalanced_producer.py" ] 

ENTRYPOINT [ "python3" ] 


