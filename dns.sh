#! /bin/bash
# Print dns servers on the client 

servers=$(cat /etc/resolv.conf | grep "nameserver" | awk '{print $2'})
arr=($servers)
for x in "${arr[@]}"; do
    echo $x
done
