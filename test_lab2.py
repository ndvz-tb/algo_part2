import unittest
from lab2 import main

class TestMinBoardSize(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(main(10, 2, 3), 9)

    def test_large_values(self):
        self.assertEqual(main(2, 1000000000, 999999999), 1999999998)

    def test_simple_square(self):
        self.assertEqual(main(4, 1, 1), 2)

if __name__ == "main":
    unittest.main()