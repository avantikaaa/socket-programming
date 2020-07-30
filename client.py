import socket
import time
import select
import sys
s = socket.socket()

host = input("Enter IP address of server: ")
port = input("Enter port: ")

#To connect to a server
s.connect((host, int(port)))

#Communication
inst=str(s.recv(1024),"utf-8")

p=int(inst[20:22])
k=0
a=str(s.recv(1024),"utf-8")
print(a)
b=str(s.recv(1024),"utf-8")
print(b)
while (k<p):
     
    data = str(s.recv(1024),"utf-8")
    if data=="bye":
    	break
    print(data)
    c,c1,c2=select.select([sys.stdin,s],[],[],20)
    if len(c)>0:
        if c[0] == sys.stdin:
            y=input()
            s.send(str.encode(y))
        else:
            d=str(c[0].recv(1024),"utf-8")
            print (d)
            k=k+1
            continue;
    data2=str(s.recv(1024),"utf-8")
    if(data2!='Answer the Question'):
    	print (data2)
    if data2=='Answer the Question':
        ans=input(data2+': ')
        time.sleep(0.25)
        s.send(str.encode(ans))
        k=k+1
        rep=str(s.recv(1024),"utf-8")
        print(rep)
    
data3=str(s.recv(1024),"utf-8")
print(data3)
