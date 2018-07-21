import time
import socket
import sys
import random
import string
import sqlite3

sqlite_file = 'urldb.sqlite'
table_name = 'urls'
id_column = 'full_url'
value_column = 'smol_url'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def main():
        network()

def network():
        connect = 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = time.time() + 60

        server_address = ('192.168.1.191', 10000)
        print('starting server on {} port {}'.format(*server_address))

        sock.bind(server_address)
        sock.listen(1)

        while connect > 0:
                print('waiting for a connection')
                connection, client_address = sock.accept()
                try:
                        print('connection from', client_address)
                        while True:
                                # close the connection after 60 seconds of uptime
                                if time.time() > timeout:
                                        connect-=1
                                        raise StopIteration
                                data = connection.recv(16)
                                print('recieved {!r}'.format(data))
                                if data:
                                        print('sending shortened url back to client')
                                        new_URL = urlEncode(data)
                                        connection.sendall(new_URL)
                                        print("INSERT INTO {tn}({idf},{vn}) VALUES ({dd},{nu})".format(tn=table_name, idf = id_column, vn = value_column, dd= '"' + str(data) + '"', nu = '"'+new_URL+'"'))
                                        c.execute("INSERT INTO {tn}({idf}, {vn}) VALUES ({dd}, {nu})".format(tn=table_name, idf = id_column, vn = value_column, dd='"'+ str(data) + '"', nu = '"'+new_URL+'"' ))
                                        conn.commit()
                                        conn.close()
                                else:
                                        print('no data from ', client_address)
                                        break
                except StopIteration: pass

        print('peace')
        connection.close()


def urlEncode(full_url):
        size = len(full_url) - 4
        filler = random.choice(string.ascii_letters + string.digits)
        filler = filler + random.choice(string.ascii_letters + string.digits)
        chunk = full_url[4:size]


        smol_url = "sm.ol/" + str(chunk[:3]) + filler
        byte_url = str.encode(smol_url)



        print(byte_url)
        return byte_url

#retrive url from database by passing in key
def urlDecode(smol_url):
        pass


if __name__ == "__main__":
        main()
