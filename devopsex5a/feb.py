import unittest

def fibonacci_series(n):
    a = 0
    b = 1
    k = 0

    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    res = [0, 1]
    while k < n - 2:
        c = a + b
        res.append(c)  # Using append instead of += for clarity
        a = b
        b = c
        k += 1

    return res

class TestFibonacciSeries(unittest.TestCase):
    def test_correct_fibonacci(self):
        self.assertEqual(fibonacci_series(5), [0, 1, 1, 2, 3])
    def test_incorrect_fibonacci(self):
        self.assertEqual(fibonacci_series(6), [0, 1, 1, 2, 3,5])
if __name__ == '__main__':
    unittest.main()
