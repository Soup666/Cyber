import threading
import socket

HOST = 'misc.bcactf.com'
PORT = 49156


def thread_function():
    print("thread starting")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for i in range(100):
            data = s.recv(1024).decode("utf-8")
            if "the letter" in data:
                s.sendall(data.split("\"")[1].encode())
            if "flag" in data or "prize" in data:
                print(data)
            if "bcactf{" in data:
                print(data)
                break
    print("thread finished")

if __name__ == "__main__":
    while True:
        threads = [threading.Thread(target=thread_function) for i in range(32)]
        for i in threads:
            i.start()
        for i in threads:
            i.join()