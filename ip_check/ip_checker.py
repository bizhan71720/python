#!/bin/python3.8

import datetime
import requests

ip_url="http://ifconfig.me"
def ip_proxy():
    proxies = {"http":"socks5:127.0.0.1:9050",\
            "https":"socks5:127.0.0.1:9050"}
    ip_proxy = requests.get(ip_url,proxies=proxies)
    return ip_proxy

def ip_normal():
    ip_normal = requests.get( ip_url)
    return ip_normal

ip_proxy = ip_proxy().content
ip_normal = ip_normal().content

date = datetime.datetime.now()
filename=str(date.year)+"-"+str(date.month)+"-"+str(date.day)

ips = str(ip_normal)[2:-1]+"/\/\\"+str(ip_proxy)[2:-1]
data = str(date.hour)+"-"+str(date.minute)+"-"+str(date.second)+"---------->"+ ips+"\n"

openfile=open(filename,"a")
openfile.write(data)
openfile.close()
