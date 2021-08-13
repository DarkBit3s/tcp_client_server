#!/usr/lib/python2.7
import socket
import getopt
import sys
def usage():

	print("-------------------TCP client------------------")
	print
	print("Usage- python tcp_client.py -t target -p port")
	print
	print
	print("Examples: ")
	print("python tcp_client.py -t 127.0.0.2 -p 1234")
	sys.exit(0) 

def main():
	if not len(sys.argv[1:]):
		usage()        
    # handle command line argument 
	try:
		opts,args = getopt.getopt(sys.argv[1:],"h:t:p:",["help","target","port"])
	except getopt.GetoptError as err:
		print(str(err))
		usage()
	port = 80
	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-t", "--target"):
			target = a
		elif o in ("-p", "--port"):
			port = int(a)
		# socket object 
		client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#connect to client 
		client.connect((target,port))
		#send data
		client.send("GET / HTTP/1.1\r\nHello Server!\r\n\r\n")   # put your msg here
		#recieve data
		responce = client.recv(55554)
		print(responce)
		client.close()
		sys.exit(0)

main()