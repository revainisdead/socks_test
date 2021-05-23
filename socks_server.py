import os
import socket


host = "127.0.0.1"
port = 8050

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)
print("Waiting for a connection...")
conn, addr = sock.accept() # blocks
# conn_id = 0

pic = "torchlight2_screenshot_copy.png"

while True:
    raw = conn.recv(1024)
    data = raw.decode("utf-8")

    print('data received: {}'.format(data))

    # first send back a response indicating how many bytes the file is
    pic_size = os.path.getsize(pic)

    if data == "f":
        with open(pic, "rb") as f:
            while True:
                b = f.read(1024)
                if not b:
                    break
                conn.send(b)
    elif data == "q":
        break

    else:
        break
