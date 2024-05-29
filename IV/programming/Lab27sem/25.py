import threading
import time

flag = threading.Event()

def seting():
    while True:
        time.sleep(2)
        flag.set()

def checking():
    while True:
        if flag.wait():
            print("Event_occurred")
            break

def retrying():
    while not flag.is_set():
        print("Event_didn't_occur")
        time.sleep(1)
thread1 = threading.Thread(target=seting)
thread2 = threading.Thread(target=checking)
thread3 = threading.Thread(target=retrying)

thread1.start()
thread2.start()
thread3.start()
thread2.join()
thread1.join()
thread3.join()
