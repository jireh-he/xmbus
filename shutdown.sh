ps -ef|grep 192.168.72.100|awk '{print $2}'| xargs kill -9
