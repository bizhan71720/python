from socket import *

s = socket(AF_INET , SOCK_STREAM)

s.bind(('127.32.25.23' , 1234))
s.listen(5)

print ("server shell running on port 1234")

c , addr = s.accept()

print ("connect to "+str(addr)+'\n')

while True :
    cmd = str(input("shell=> "))
    c.sendall(cmd)
    cmd_output = c.recv(12345)
    print (cmd_output)
    print ()

c.close()
