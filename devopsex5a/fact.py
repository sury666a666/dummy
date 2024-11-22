import unittest

def fact(n):
    if n < 0:
        return "cannot find the factorial for negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
class TestFactorial(unittest.TestCase):
    def test_correct_factorial(self):
        self.assertEqual(fact(5), 120) 
    def test_incorrect_factorial(self):
        self.assertEqual(fact(5), 125) 
if __name__ == '__main__':
    unittest.main()
