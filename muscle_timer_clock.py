import urllib3
import select
import selectors
import time
import threading


def func():
    print("======>hello")


def loop():
    print("======>loop")
    threading.Timer(1, func, args=None, kwargs=None).start()


if __name__ == '__main__':
    loopThread = threading.Thread(name="looper", daemon=True, target=loop)
    loopThread.start()
    while True:
        pass
        # print("wile true")