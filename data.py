import requests
import json
import csv
r=requests.get(url='http://20.0.0.254:8888/servers/sample/stats')
data={}
data["stats"]=r.json()
#r=requests.get(url='http://20.0.0.254:8888/servers/')
#data["servers"]=r.json()
#r=requests.get(url='http://20.0.0.254:8888/servers/sample')
#data["server_arrangements"]=r.json()
with open('/tngbench_share/go_data.json','w') as f:
    json.dump(data,f,separators=(',',':'),indent=None)