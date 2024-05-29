import threading

class Queue:
    def __init__(self):
        self.queue = []
        self.lock = threading.RLock()

    def enqueue(self, item):
        with self.lock:
            self.queue.append(item)
            print("Added", item)

    def dequeue(self):
        with self.lock:
            if self.queue:
                item = self.queue.pop(0)
                print("Deleted", item)
                return item
            else:
                print("Empty...Nothing to delete")
                return None

def worker(queue):
    while True:
        item = queue.dequeue()
        if item is None:
            break

def main():
    queue = Queue()
    for i in range(1, 6):
        queue.enqueue(i)

    workers = []
    for _ in range(3):
        t = threading.Thread(target=worker, args=(queue,))
        t.start()
        workers.append(t)

    for t in workers:
        t.join()

if __name__ == "__main__":
    main()
