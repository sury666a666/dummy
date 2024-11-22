

class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, val):
        if self.is_full():
            print("Queue overflow")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = val
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def get_size(self):
        return self.count

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        return "Queue is empty!"

    def print_queue(self):
        print("Current Queue:", self.queue)

import unittest
class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue() 
        self.assertEqual(q.get_size(), 2)
        self.assertEqual(q.peek(), 2)
        q.print_queue()
if __name__ == '__main__':
    unittest.main()
