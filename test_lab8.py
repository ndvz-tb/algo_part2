import unittest
from lab8 import calculate_max_wire

class TestWireCalculation(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(calculate_max_wire(2, [3, 3, 3]), 5.66)

    def test_example_2(self):
        self.assertEqual(calculate_max_wire(100, [1, 1, 1, 1]), 300.00)

    def test_example_3(self):
        self.assertEqual(calculate_max_wire(4, [100, 2, 100, 2, 100]), 396.32)

    def test_example_4(self):
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        self.assertEqual(calculate_max_wire(4, heights), 2738.18)

if __name__ == '__main__':
    unittest.main()