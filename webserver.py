import socket

#Prepare a server socket
HOST, PORT = '', 80

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, \
                            socket.IPPROTO_TCP)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('', 80))
listen_socket.listen(1)

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = listen_socket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])

        connectionSocket.sendall("""HTTP/1.1 200 OK
Content-Type: text/html

""")
        connectionSocket.send(f.read())
        print 'Valid request'
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        print '404 no such file'
        connectionSocket.sendall("""HTTP/1.1 404 Not Found
Content-Type: text/html

<html>
<head>
<title>Not Found</title>
</head>
<body>
The file/page was not found.
</body>
</html>
""")
        connectionSocket.close()
listen_socket.close() 
