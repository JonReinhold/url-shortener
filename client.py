import socket

# hard code private IP of linux box
ip = '192.168.1.191'
port = 10000
buffer_size = 1024
message = input("Enter URL to smol-ify: ")
message = str.encode(message)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(message)
data = s.recv(buffer_size)
s.close()

prettyURL = (str(data).replace("'",""))
print(prettyURL[2:-1])
