import csv
import requests
import sys
# logic inspired by https://github.com/RobustPerception/python_examples/blob/master/csv/query_csv.py
"""
A simple program to print the result of a Prometheus query as CSV.
@ Author: Bhubanesh Mishra
"""

if len(sys.argv) != 3:
    #print('Usage: {0} http://prometheus:9090 a_query'.format(sys.argv[0]))
    #print('Usage: {0} http://localhost:9090 a_query'.format(sys.argv[0]))
    print('Usage: {0} http://54.242.198.153:9090 a_query'.format(sys.argv[0]))
    sys.exit(1)

response = requests.get('{0}/api/v1/query'.format(sys.argv[1]),
        params={'query': sys.argv[2]})
fetchdata = response.json()['data']['result']

# Build a list of all query metrics names used.
querynames = set()
for val in fetchdata:
      querynames.update(val['metric'].keys())

# Canonicalize the extracted query metrics names
querynames.discard('__name__')
querynames = sorted(querynames)
writer = csv.writer(sys.stdout)
# Write the header,
writer.writerow(['name', 'timestamp', 'values'] + querynames)

# Write the samples.
for val in fetchdata:
    l = [val['metric'].get('__name__', '')] + val['value']
    for query in querynames:
        l.append(val['metric'].get(query, ''))
    writer.writerow(l)
