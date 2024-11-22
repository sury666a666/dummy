import unittest

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def take_out(self, amount):
        self.balance -= amount
        return self.balance

class TestBank(unittest.TestCase):
    def test_deposit_correct_1(self):
        bank_obj = Bank(10000)
        self.assertEqual(bank_obj.deposit(1200), 11200)
    def test_take_out_correct_1(self):
        bank_obj = Bank(10000)
        self.assertEqual(bank_obj.take_out(200), 9800)
    def test_deposit_take_out_correct_2(self):
        bank_obj = Bank(10000)
        self.assertEqual(bank_obj.deposit(3400), 13400)
        self.assertEqual(bank_obj.take_out(4000), 9400)
if __name__ == '__main__':
    unittest.main()
