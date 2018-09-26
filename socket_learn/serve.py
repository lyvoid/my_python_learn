import socket
import queue
import threading


def worker():
    while True:
        i = q.get()
        conn, addr = i
        while 1:
            sms = conn.recv(1024).decode('utf-8')
            if sms != "":
                print("Message from (" + str(addr[0]) + ":" + str(addr[1]) + "): " + sms)
            else:
                print("Close the Connection from (" + str(addr[0]) + ":" + str(addr[1]) + ")")
                conn.close()
                break
        q.task_done()


if __name__ == "__main__":
    q = queue.Queue()
    thread_num = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("192.168.2.47", 4242))
    s.listen(50000)
    print("Server is listening at 4242")

    for _ in range(0, thread_num):
        t = threading.Thread(target=worker)
        t.setDaemon(1)
        t.start()

    while 1:
        conn, addr = s.accept()
        print("Connection come from (" + str(addr[0]) + ":" + str(addr[1]) + ")")
        q.put((conn, addr))

    q.join()
