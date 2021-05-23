import os
import socket


# netstat -an

host = "127.0.0.1"
port = 8050

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

buff = 4096

recv_total = 0
while True:
    msg = input("Your message: ")

    sock.send(msg.encode("utf-8"))

    if msg == "f":
        new_filename = "post_socket_pic.png"

        # if file exists, delete it first
        try:
            os.remove(new_filename)
        except OSError:
            pass

        # ab - append bytes
        with open(new_filename, "ab+") as fout:
            while True:
                d = sock.recv(buff)

                fout.write(d)

                recv_total += len(d)
                print(recv_total)

                if recv_total == 922542:
                    break




    elif msg == "q":
        break
