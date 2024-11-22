import unittest

def anagram(s1, s2):
    y = {}
    m = {}

    for i in s1:
        if i in y:
            y[i] += 1
        else:
            y[i] = 1

    for i in s2:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1

    if m == y:
        return "anagram"
    else:
        return "not anagram"

class TestAnagram(unittest.TestCase):
    def test_anagram_correct_1(self):
        self.assertEqual(anagram('listen', 'silent'), "anagram")
    def test_anagram_correct_2(self):
        self.assertEqual(anagram('hello', 'world'), "not anagram")
if __name__ == '__main__':
    unittest.main()
