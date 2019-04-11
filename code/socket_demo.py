import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 80))
sk.listen()


while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    print(data)
    conn.send(b"OK")
    conn.close()
