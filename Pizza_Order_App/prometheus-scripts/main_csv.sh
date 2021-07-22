#!/bin/bash
. /home/ubuntu/prometheus-scripts/broker0/mem_usage.sh
. /home/ubuntu/prometheus-scripts/broker0/cpu_usage.sh
. /home/ubuntu/prometheus-scripts/broker0/ir.sh
. /home/ubuntu/prometheus-scripts/broker0/or.sh
sleep 1
. /home/ubuntu/prometheus-scripts/broker1/mem_usage.sh
. /home/ubuntu/prometheus-scripts/broker1/cpu_usage.sh
. /home/ubuntu/prometheus-scripts/broker1/ir.sh
. /home/ubuntu/prometheus-scripts/broker1/or.sh
sleep 1
. /home/ubuntu/prometheus-scripts/broker2/mem_usage.sh
. /home/ubuntu/prometheus-scripts/broker2/cpu_usage.sh
. /home/ubuntu/prometheus-scripts/broker2/ir.sh
. /home/ubuntu/prometheus-scripts/broker2/or.sh
