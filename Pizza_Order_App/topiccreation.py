# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:30:29 2021

@author: Bhuvi
"""

#import datetime as dt
import logging
#from collections import defaultdict
from typing import List
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.protocol.admin import Response

LOG: logging.Logger = logging.getLogger("kafka-topic-loader.topic")

def create_topics(
    kafka_admin_client: KafkaAdminClient,
    no_of_topics: int,
    per_topic_partition: int,
    no_of_replicas_per_partition: int,
    timeout_ms: int,
    base_topic_name: str,
    max_batch_size: int = 50
    
) -> List[Response]:

 #   batches: List[List[NewTopic]] = []
     
    LOG.info(
        "Create %d topics each with %d partitions which are replicated %d times",
        no_of_topics,
        per_topic_partition,
        no_of_replicas_per_partition,
    )

    #prefix: str = dt.datetime.utcnow().strftime("%H-%M")
    
    LOG.info("Create topic objects")
    
    topic_list: List[NewTopic] = []
    #This functionality will prep new topic for addition if topic doesn't exist
    broker_topics = kafka_admin_client.list_topics()
    print(broker_topics)
    for i in range(1, no_of_topics+1):
        Exists=False
        LOG.debug("Creating topic object %d", i)
        name=f"{base_topic_name}-{i}"
        for j in (broker_topics):
            #if j.topics.get(j.topic_name)==name:
            if j == name:
                Exists=True
                break
        if not Exists:
            topic_list.append(
                NewTopic(
                    name=name,
                    num_partitions=per_topic_partition,
                    replication_factor=no_of_replicas_per_partition,
                )
            )

    LOG.info("Batch the topic objects")
    topic_batches: List[List[NewTopic]] = []
    topic_batch: List[NewTopic] = []
    for i, topic in enumerate(topic_list):
        if i % max_batch_size <= 0:
            if topic_batch:
                topic_batches.append(topic_batch)
            topic_batch = []
        topic_batch.append(topic)
    topic_batches.append(topic_batch)

    batch_creation_responses: List[Response] = []
    for i, topic_batch in enumerate(topic_batches):
        LOG.info("Submitting topic batch %d (size %d) to Kafka Admin Client for creation",
                 i, len(topic_batch))
        response: Response = kafka_admin_client.create_topics(
            new_topics=topic_batch, validate_only=False, timeout_ms=timeout_ms
        )
        batch_creation_responses.append(response)

    return batch_creation_responses


def execute_topic_creation(
    base_topic_name: str,
    no_of_topics: int,
    per_topic_partition: int,
    no_of_partition_per_replicas: int,
    response_timeout: int = 60000,
) -> List[str]:

    LOG.debug("Create Kafka Admin Client")
    kafka_admin_client: KafkaAdminClient = KafkaAdminClient(
        bootstrap_servers='10.105.85.14:9099',
        client_id="topic-creator",
        metadata_max_age_ms=response_timeout,
    )

    topic_list: List[str] = []
    #Will populate the list with pre-existing topics matching naming conventions
    broker_topics = kafka_admin_client.list_topics()
    for i in range(1,no_of_topics+1):
        Exists=False
        name=f"{base_topic_name}-{i}"
        for j in (broker_topics):
           # if j.topics.get(j.topic_name)==name:
            if j == name:
                Exists=True
                break
        if Exists:
            topic_list.append(name)

    responses: List[Response] = create_topics(
        kafka_admin_client,
        no_of_topics,
        per_topic_partition,
        no_of_partition_per_replicas,
        timeout_ms=response_timeout,
        base_topic_name=base_topic_name
    )
    
    
    for batch_response in responses:
        for topic_error in batch_response.topic_errors:
            if topic_error[2] is None:
                topic_list.append(topic_error[0])
            else:
                LOG.error("Error in topic %s", topic_error[0])

    LOG.debug("Closing Kafka Admin Client")
    kafka_admin_client.close()

    return topic_list

