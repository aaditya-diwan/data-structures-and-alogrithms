class Queue:
    def __init__(self):
        self._queue = []
    
    def enqueue(self, data):
        self._queue.append(data)
    
    def dequeue(self):
        return self._queue.pop(0)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())