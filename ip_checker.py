#!/bin/python3.8

import datetime
import requests

ip_url="http://ifconfig.me"

def ip_proxy():
    try:
        proxies = {"http":"socks5:127.0.0.1:9050",\
                "https":"socks5:127.0.0.1:9050"}
        ip_proxy = requests.get(ip_url,proxies=proxies).content
        
    except:
        ip_proxy = "**proxy service is not active this time*"

    return ip_proxy

def ip_normal():
    try:
        ip_normal = requests.get( ip_url).content
        
    except:
        ip_normal = "**internet connection refused*"
    return ip_normal

ip_proxy = ip_proxy()
ip_normal = ip_normal()

date = datetime.datetime.now()
filename=str(date.year)+"-"+str(date.month)+"-"+str(date.day)+".txt"#can add your path in first of this string

ips = str(ip_normal)[2:-1]+"\t/\/\\\t"+str(ip_proxy)[2:-1]
data = str(date.hour)+":"+str(date.minute)+"\t──────────>\t"+ ips+"\n"

of = open(filename, 'a')
of.write(data)
of.close()