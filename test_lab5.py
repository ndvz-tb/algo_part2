import unittest
from lab5 import calculate_marriages

class TestTribalMarriages(unittest.TestCase):
    """
    Набір юніт-тестів для перевірки алгоритму пошуку міжплемінних шлюбів.
    """

    def test_example_1(self):
        n = 3
        edges = [
            (1, 2),
            (2, 4),
            (3, 5)
        ]
        self.assertEqual(calculate_marriages(n, edges), 4)

    def test_example_2(self):
        n = 5
        edges = [
            (1, 2),
            (2, 4),
            (1, 3),
            (3, 5),
            (8, 10)
        ]
        self.assertEqual(calculate_marriages(n, edges), 6)

    def test_all_boys(self):
        n = 2
        edges = [
            (1, 3),
            (5, 7)
        ]
        self.assertEqual(calculate_marriages(n, edges), 0)
        
    def test_no_valid_pairs_in_one_tribe(self):
        n = 2
        edges = [
            (1, 2),
            (2, 3)
        ]
        self.assertEqual(calculate_marriages(n, edges), 0)

if __name__ == '__main__':
    unittest.main()