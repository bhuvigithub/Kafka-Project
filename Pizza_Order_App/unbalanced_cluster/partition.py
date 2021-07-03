# -*- coding: utf-8 -*-
"""
Created on Sat June 26 13:35:19 2021

@author: Bhuvi
"""
import logging
#import math


from collections import defaultdict
from typing import List, Set, Dict, DefaultDict

from kafka.admin import KafkaAdminClient
from kafka.structs import PartitionMetadata

LOG: logging.Logger = logging.getLogger("kafka-topic-loader.topic")

NEGLECT_TOPICS = ["__", "strimzi"]

# inspired from https://github.com/tomncooper/kafka-topic-loader/blob/master/topics.py
def get_partitions(
    kafka_admin_client: KafkaAdminClient= KafkaAdminClient(
        bootstrap_servers='10.105.85.14:9099'
        ),
) -> Dict[str, Dict[int, PartitionMetadata]]:

    return kafka_admin_client._client.cluster._partitions


def sorting_partitions_by_leader(
    kafka_admin_client: KafkaAdminClient= KafkaAdminClient(
        bootstrap_servers='10.105.85.14:9099'
        ),
) -> Dict[str, Dict[int, List[int]]]:
    """ This method produces a dictionary which maps from topic of string type to node id to that of a
    list of partition ids for those partitions whose leader replica is on that node.
    """

    LOG.info("Sorting partitions by leader")

    partition_metadata: PartitionMetadata = get_partitions(kafka_admin_client)

    loaded_topics: List[str] = get_loaded_topics(kafka_admin_client=kafka_admin_client)

    tnpart: Dict[str, Dict[int, List[int]]] = {}

    for topic, prtn_dict in partition_metadata.items():
        if topic in loaded_topics:
            node_partiton_leader: DefaultDict[int, List[int]] = defaultdict(list)
            for partition, partmd in prtn_dict.items():
                node_partiton_leader[partmd.leader].append(partition)
            tnpart[topic] = dict(node_partiton_leader)

    return tnpart


def get_loaded_topics(kafka_admin_client: KafkaAdminClient) -> List[str]:

    LOG.info("Fetching the topic names")
    topics: Set[str] = kafka_admin_client._client.cluster.topics(exclude_internal_topics=True)

    LOG.debug("Creating the Kafka Admin Client")
    kafka_admin_client.close()

    return [topic for topic in topics
            if not any([True for excluded in NEGLECT_TOPICS if excluded in topic])]



