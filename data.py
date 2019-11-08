import requests
import json
import csv
r=requests.get(url='http://20.0.0.254:8888/servers/sample/stats')
data={}
data["stats"]=json.loads(r.json())
r=requests.get(url='http://20.0.0.254:8888/servers/')
data["servers"]=json.loads(r.json())
r=requests.get(url='http://20.0.0.254:8888/servers/sample')
data["server_arrangements"]=json.loads(r.json())
with open('/tngbench_share/data.txt','w') as f:
    json.dump(data,f)
with open('/tngbench_share/go_data.csv', 'w') as f:
    for key in data.keys():
        f.write("%s,%s\n"%(key,data[key]))

with open('/tngbench_share/go_data.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, data.keys())
    w.writeheader()
    w.writerow(data)