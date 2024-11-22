import unittest

class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def push(self, val):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.stack[self.top] = val

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return
        popped_value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return popped_value

    def is_full(self):
        return self.top == self.size - 1

    def is_empty(self):
        return self.top == -1

    def get_size(self):
        return self.top + 1

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        return "Stack is empty!"

    def print_stack(self):
        print("Current Stack:", self.stack)

class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack(3)
        s.push(10)
        s.push(20)
        s.push(30)
        s.print_stack()
        self.assertEqual(s.get_size(), 3) 
        self.assertEqual(s.peek(), 30)    
if __name__ == '__main__':
    unittest.main()
