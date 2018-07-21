require 'socket'

# URL input 
puts "URL to shorten: "
url = gets

#socket creation 
socket = TCPSocket.new "192.168.1.191", 10000
socket.puts url

# read and close
response = socket.select
socket.close

puts response
