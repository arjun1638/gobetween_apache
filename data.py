import requests
import json
r=requests.get(url='http://20.0.0.254:8888/servers/sample/stats')
with open('/tngbench_share/gob-servers-stat-data.txt','w') as f:
    json.dump(r.json(),f)