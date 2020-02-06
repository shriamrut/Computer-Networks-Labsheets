import socket
s=socket.socket()
port=12345
host=socket.gethostname()
s.connect((host,port))
message="hello.txt"
s.sendto(message.encode(),(host,port))
output=open("write.txt","w+")
while 1:
	response=s.recv(1024)
	if not response:
		break
	print(response.decode())
	output.write(response.decode())
s.close()
