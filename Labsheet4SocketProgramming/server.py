#in browser localhost:12345/filename_requested
#assumption is that the requested file is present in the Desktop
import socket
import os
port=12345
s=socket.socket()
s.bind(('',port))
s.listen(5)
print("Server is Listening")
while True:
	conn,addr=s.accept()
	print("Got connection from "+str(addr))
	data=conn.recv(1024)
	print("Server received "+str(repr(data)))
	reqpath=data.decode().split()[1]
	try:
		f=open("/home/examuser/Desktop/"+reqpath)
		siz=os.path.getsize("/home/examuser/Desktop/"+reqpath)
		responsedata=f.read(siz)
		conn.send((responsedata).encode())
	except Exception as e:
		print("File not found. Error 404")
		response+="\nFile not found. Error 404"
	finally:
		conn.close()
		break
