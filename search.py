import splunklib.client as client
import splunklib.results as results

s = client.connect(host='192.168.40.138', port=8089, username='admin',password='1q2w3e4r!')
jobs = s.jobs
query="search index=botsv2 earliest=0 | head 2"
rr = s.jobs.oneshot(query)
print('query succeed')

    #read results
reader = results.ResultsReader(rr)
for item in reader:
        print(item['_time'])
