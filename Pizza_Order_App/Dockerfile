FROM python:3

ADD producer_pizza.py /

ADD consumer_pizza.py /

ADD envconfig.py /

ADD pizzaapp_consumer.py /

ARG KAFKA_TOPIC_NAME=new-pizza-orders

ARG KAFKA_NO_OF_MESSAGES=0

ARG KAFKA_MAX_WAIT_TIME=1

ENV TOPIC_NAME=$KAFKA_TOPIC_NAME

ENV NO_OF_MESSAGES=$KAFKA_NO_OF_MESSAGES

ENV MAX_WAIT_TIME=$KAFKA_MAX_WAIT_TIME

RUN pip install kafka

RUN pip install kafka-python

RUN pip install faker

RUN pip install python-decouple

CMD [ "python", "./envconfig.py" ]

