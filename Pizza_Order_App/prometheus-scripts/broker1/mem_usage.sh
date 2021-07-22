#!/bin/bash
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[5m])' >> /home/ubuntu/prometheus-scripts/results/broker1_mem.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[15m])' >> /home/ubuntu/prometheus-scripts/results/broker1_mem.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[30m])' >> /home/ubuntu/prometheus-scripts/results/broker1_mem.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[1h])' >> /home/ubuntu/prometheus-scripts/results/broker1_mem.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[5m]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggmem.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[15m]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggmem.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[30m]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggmem.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(rate(container_memory_usage_bytes{namespace="kafka",pod="my-cluster-metrics-kafka-1",container="kafka"}[1h]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggmem.csv
