import csv
import requests
import sys
# inspired by https://github.com/RobustPerception/python_examples/blob/master/csv/query_csv.py
"""
A simple program to print the result of a Prometheus query as CSV.
"""

if len(sys.argv) != 3:
    #print('Usage: {0} http://prometheus:9090 a_query'.format(sys.argv[0]))
    #print('Usage: {0} http://localhost:9090 a_query'.format(sys.argv[0]))
    print('Usage: {0} http://54.242.198.153:9090 a_query'.format(sys.argv[0]))
    sys.exit(1)

response = requests.get('{0}/api/v1/query'.format(sys.argv[1]),
        params={'query': sys.argv[2]})
#results = response.json()['data']['result']
fetchdata = response.json()['data']['result']
#print(fetchdata)

# Build a list of all labelnames used.
#labelnames = set()
querynames = set()
#for result in results:
for val in fetchdata:
      #labelnames.update(result['metric'].keys())
      querynames.update(val['metric'].keys())
# Canonicalize
#labelnames.discard('__name__')
querynames.discard('__name__')
#labelnames = sorted(labelnames)
querynames = sorted(querynames)
#print(querynames)
writer = csv.writer(sys.stdout)
# Write the header,
#writer.writerow(['name', 'timestamp', 'values'] + labelnames)
writer.writerow(['name', 'timestamp', 'values'] + querynames)

# Write the sanples.
#for result in results:
for val in fetchdata:
    #l = [result['metric'].get('__name__', '')] + result['values']
    l = [val['metric'].get('__name__', '')] + val['values']
    #for label in labelnames:
    for query in querynames:
        #l.append(result['metric'].get(label, ''))
        l.append(val['metric'].get(query, ''))
    writer.writerow(l)
