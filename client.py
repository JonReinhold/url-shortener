import socket

ip = '192.168.1.191'
port = 10000
buffer_size = 2000

# CLI mode
# message = input("Enter URL to smol-ify: ")

file = open("C:\\Users\\Admin\\Downloads\\URL_To_Shorten.txt", "r")
message = file.read()
message = str.encode(message)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(message)
data = s.recv(buffer_size)
s.close()

prettyURL = (str(data).replace("'",""))
print(prettyURL[2:-1])
