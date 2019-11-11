python ./data.py 

sleep 2
python ./log_intf_statistics.py /tngbench_share/result.yml

sleep 2
python ./process_ab_results.py /tngbench_share/cmd_start.log /tngbench_share/go_data.json /tngbench_share/result.yml


date > /mnt/share/stop.txt