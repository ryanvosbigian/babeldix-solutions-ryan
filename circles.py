import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",1234))
s.sendall('"circles"\n')
recv = ""
while "\n" not in recv:
	recv = recv + s.recv(4096)
recv = recv.strip()
recvlist = []
exec "recvlist =" +  recv

def incircle(circle_coord,rand_x,rand_y):
	if (rand_x - circle_coord[0])**2 + (rand_y - circle_coord[1])**2 < circle_coord[2]**2: #if dart inside circle
		return True
	return False
NUMBER_OF_DARTS = 10000

darts_outside_all_circles = 0.0
for repeat in range(NUMBER_OF_DARTS):
	rand_x = random.random()
	rand_y = random.random()
	dart_outside_circles = True
	for circle_coord in recvlist:
		if incircle(circle_coord,rand_x,rand_y):
			dart_outside_circles = False
	if dart_outside_circles:
		darts_outside_all_circles+=1

answer = float(darts_outside_all_circles)/float(NUMBER_OF_DARTS)

s.sendall('%s\n'%(str(answer)))
recv = s.recv(4096)
print "ANSWER:"+str(answer)
print "MESSAGE: %s"%(recv)

