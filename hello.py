import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",1234))

s.sendall('"hello"\n')
print "SENT 'hello'"

recv = s.recv(4096)

print "MESSAGE: %s"%(recv)


s.sendall('"goodbye"\n')
print "SENT 'goodbye'"
