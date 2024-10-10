import threading


def funcName(i):
    print(i)

if __name__ == "__main__":
    for i in range(10):
        th = threading.Thread(funcName(i))
        th.start()
        th.join()
    print(threading.active_count())
    