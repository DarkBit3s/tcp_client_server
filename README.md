# tcp_client_server
TCP client server is used inside a single computer or different computers to test there services.
This is a python based tcp client program used to test for services, sending garbage data, fuzz, or other testing tasks. It is useful in when you don't have luxary of networking tools ot compilers and missing copy paste option or don't have internet connection.
run the client code as:
 <i><b>python tcp_client.py --help</b></i>
 <br><h1>NOTE</h1>
 if you test this on localhost first start the APACHE server on your machine otherwise it wont work or if there is a service running on your localhost you can gic ethe port of that service to test.
 <h3><b>service apache2 start</b></h3>
 then run python script on this port.
In this code we making assumption about socket that this connection given always works and server is always expecting us to send data back to us.
TCP server code is same as tcp client code. TCP server is used when writing commands shell or crafting a proxy. 
 <i><b>python tcp_server.py</b></i>
in practice case the TCP_client and tcp_server code run like this:
