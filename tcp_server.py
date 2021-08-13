import socket
import threading 

host_ip = "127.0.0.2"
host_port = 80

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host_ip,host_port))
server.listen(5)

print("[*] Listening on %s:%d" % (host_ip,host_port))

#client handling thread
def handle_client(client_socket):
	# print what client send to us
	request = client_socket.recv(1024)

	print("[*] Recived %s" %request)
	#send acknowladgement packet

	client_socket.send("ACK")  # put your message here
	client_socket.close()

while True:
	client,addr = server.accept()
	print(client)
	print("[*] Accepted connection from %s:%d"%(addr[0],addr[1]))
	#spin up our client thread to handle incoming connection
	client_handle = threading.Thread(target=handle_client,args=(client,))
	client_handle.start()
