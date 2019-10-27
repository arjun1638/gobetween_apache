Gobetween with 3 Apache servers

Just use the docker-compose.yaml file and build it .
- 'docker-compose up --build -d'

You can change ip allocation/server images in docker compose file
please note if you change the ip-address, also update them in '/etc/gobetween/conf/gobetween.toml' so that traffic can be send accordingly with ip.

You can generate the traffic using apache bench using command e.g 
    - ' ab -n 100 -c 100 http://172.20.0.5:3000/'

Gobetween json output stat can be seen at 
    -'http://172.20.0.5:8888/servers/sample/stats'
    

Gobetween Repo cloned and modified from : https://github.com/yyyar/gobetween
