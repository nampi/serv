import socket
import threading
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',2222))
s.listen(10)

def server(conn, addr):
    #s.listen(10)
    while True:
        #conn, addr=s.accept()
        #while True:
        data=conn.recv(1024)
        if not data: break
        if data == b"close": break
        conn.send(data)
    conn.close()


while True:
    conn, addr = s.accept()
    #print("Connection", addr)
    #t = threading.Thread(target=server, args=(conn, addr))
    #t.start()
    thread.start_new_thread(server, (conn,))
    #server(conn, addr)
