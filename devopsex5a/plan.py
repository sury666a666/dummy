import unittest

def palindrome(s1):
    if s1 == s1[::-1]:
        return True
    else:
        return False
class TestPalindrome(unittest.TestCase):
    def test_palindrome_correct_1(self):
        self.assertTrue(palindrome('radar'))  
    def test_palindrome_correct_2(self):
        self.assertFalse(palindrome('hello'))  
if __name__ == '__main__':
    unittest.main()
