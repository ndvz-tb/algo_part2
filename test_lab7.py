import unittest
import os
from lab7 import get_minimum_cable_length

class TestCableRouting(unittest.TestCase):

    def setUp(self):
        with open("test_normal.txt", "w", encoding="utf-8") as f:
            f.write("K1,K2,2000\nK2,K3,1500\nK1,K3,3000\n")

        with open("test_disconnected.txt", "w", encoding="utf-8") as f:
            f.write("K1,K2,2000\nK3,K4,1500\n")

        with open("test_empty.txt", "w", encoding="utf-8") as f:
            f.write("")

    def tearDown(self):
        files_to_remove = ["test_normal.txt", "test_disconnected.txt", "test_empty.txt"]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def test_normal_connection(self):
        result = get_minimum_cable_length("test_normal.txt")
        self.assertEqual(result, 3500)

    def test_disconnected_wells(self):
        result = get_minimum_cable_length("test_disconnected.txt")
        self.assertEqual(result, -1)

    def test_empty_file(self):
        result = get_minimum_cable_length("test_empty.txt")
        self.assertEqual(result, 0)

    def test_file_not_found(self):
        result = get_minimum_cable_length("missing_file.txt")
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()