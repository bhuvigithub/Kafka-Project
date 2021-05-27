FROM python:3

ADD producer_pizza.py /

ADD consumer_pizza.py /

ADD envconfig.py /

ADD pizzaapp_consumer.py /

RUN pip install kafka

RUN pip install kafka-python

RUN pip install faker

RUN pip install python-decouple

CMD [ "python", "./envconfig.py" ]

