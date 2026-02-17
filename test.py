import unittest
from lab1_part2 import find_unsorted_subarray

class TestLab1(unittest.TestCase):

    def test_example_from_task(self):
        """Тест із прикладу в завданні"""
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(find_unsorted_subarray(arr), (3, 9))

    def test_already_sorted(self):
        """Вхідний масив посортований"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_unsorted_subarray(arr), (-1, -1))

    def test_sort_entire_array(self):
        """Масив необхідно сортувати весь"""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(find_unsorted_subarray(arr), (0, 4))

    def test_single_element(self):
        """Масив містить лише 1 елемент"""
        self.assertEqual(find_unsorted_subarray([1]), (-1, -1))

if __name__ == '__main__':
    unittest.main()