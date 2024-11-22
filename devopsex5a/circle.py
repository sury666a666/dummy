import unittest

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

class TestCircle(unittest.TestCase):
    def test_area_correct_1(self):
        circle_obj = Circle(1.2)
        self.assertAlmostEqual(circle_obj.area(), 4.5216, places=4)
    def test_circumference_correct_1(self):
        circle_obj = Circle(1.2)
        self.assertAlmostEqual(circle_obj.circumference(), 7.536, places=3)
    def test_area_circumference_correct_2(self):
        circle_obj = Circle(5.2)
        self.assertAlmostEqual(circle_obj.area(), 84.9056, places=4)
        self.assertAlmostEqual(circle_obj.circumference(), 32.656, places=3)
if __name__ == '__main__':
    unittest.main()
X