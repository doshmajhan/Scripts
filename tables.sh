# !/bin/bash

iptables -F

iptables -A OUTPUT -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

#Loopback
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

#SSH
iptables -A INPUT -i eth0 -p tcp -s 129.21.0.0/16 --dport 22 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp -s 129.21.0.0/16 --sport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp -s 129.21.0.0/16 --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp -s 129.21.0.0/16 --sport 22 -m state --state ESTABLISHED -j ACCEPT

#Allow laptop
iptables -A INPUT -i eth0 -p tcp --dport 22 -m mac --mac-source B8:27:EB:A5:A6:8A -j ACCEPT

#Web
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT

#FTP
iptables -A OUTPUT -p tcp --dport 21 -j ACCEPT
iptables -A INPUT -p tcp --sport 21 -j ACCEPT
iptables -A INPUT -p tcp --sport 20 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 20 -j ACCEPT

#DNS
iptables -A OUTPUT -p udp --sport 53 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p udp --sport 53 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT

#iptables -A OUTPUT -p udp --sport 9999 -j ACCEPT
#iptables -A INPUT -p udp --dport 9999 -j ACCEPT
#iptables -A INPUT -p udp --sport 9999 -j ACCEPT
#iptables -A OUTPUT -p udp --dport 9999 -j ACCEPT


#Ping
iptables -A OUTPUT -p icmp --icmp-type 8 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type 0 -j ACCEPT

#NTP
iptables -A OUTPUT -p udp --sport 123 -j ACCEPT
iptables -A INPUT -p udp --dport 123 -j ACCEPT
iptables -A OUTPUT -p udp --dport 123 -j ACCEPT
iptables -A INPUT -p udp --sport 123 -j ACCEPT

iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP
