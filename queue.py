class Queue:
    def __init__(self, max_size=100):
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.max_size = max_size

    def enqueue(self, item):
        if self.rear == self.max_size:
            print("Queue is full.")
            return
        self.queue[self.rear] = item
        self.rear += 1
    def dequeue(self):
        if self.front == self.rear:
            return "Queue is empty!"
        item = self.queue[self.front]

        for i in range(self.front, self.rear - 1):
            self.queue[i] = self.queue[i + 1]
        self.queue[self.rear - 1] = None 
        self.rear -= 1
        return item

    def is_empty(self):
        return self.front == self.rear
    
    def size(self):
        return self.rear - self.front

    def peek(self):
        if self.front == self.rear:
            return "Queue is empty!"
        return self.queue[self.front]
    def printque(self):
        for i in range(self.size()):
            print(self.queue[self.front])

if __name__ == "__main__":
    q = Queue(max_size=5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    q.printque()
