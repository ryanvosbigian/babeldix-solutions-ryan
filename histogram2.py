import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",1234))
s.sendall('"histogram"\n')
recv = ""
while "\n" not in recv:
	recv = recv + s.recv(4096)
recv = recv.strip()
recvlist = []
exec "recvlist =" +  recv
print recvlist
recvlist[1].sort()
amounts = [0 for each in range(recvlist[0][0])]
for each in recvlist[1]:
	amounts[each/recvlist[0][1]] +=1

s.sendall('%s\n'%(str(amounts)))
recv = s.recv(4096)
print amounts
print "MESSAGE: %s"%(recv)