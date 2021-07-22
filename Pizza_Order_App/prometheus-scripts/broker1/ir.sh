#!/bin/bash
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[5m])' >> /home/ubuntu/prometheus-scripts/results/broker1_irate.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[15m])' >> /home/ubuntu/prometheus-scripts/results/broker1_irate.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[30m])' >> /home/ubuntu/prometheus-scripts/results/broker1_irate.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[1h])' >> /home/ubuntu/prometheus-scripts/results/broker1_irate.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[5m]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggirate.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[15m]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggirate.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[30m]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggirate.csv
sleep 2
python3 /home/ubuntu/prometheus-scripts/query2csv.py http://localhost:9090 'sum(irate(kafka_server_brokertopicmetrics_bytesin_total{namespace="kafka",strimzi_io_cluster="my-cluster-metrics",kubernetes_pod_name=~"my-cluster-metrics-kafka-1"}[1h]))' >> /home/ubuntu/prometheus-scripts/results/broker1_aggirate.csv
