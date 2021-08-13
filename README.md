# tcp_client_server
TCP client server is used inside a single computer or different computers to test there services.
This is a python based tcp client program used to test for services, sending garbage data, fuzz, or other testing tasks. It is useful in when you don't have luxary of networking tools ot compilers and missing copy paste option or don't have internet connection.
run the client code as:
 <i><b>python tcp_client.py --help</b></i>
In this code we making assumption about socket that this connection given always works and server is always expecting us to send data back to us.
TCP server code is same as tcp client code. TCP server is used when writing commands shell or crafting a proxy. 
****python tcp_server.py****
in practice case the TCP_client and tcp_server code run like this:
