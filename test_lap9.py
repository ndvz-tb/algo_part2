import unittest
from lab9 import kmp_search 

class TestKMPSearch(unittest.TestCase):

    def test_standard_match(self):

        self.assertEqual(kmp_search("ABABDABACDABABCABAB", "ABABCABAB"), [10])

    def test_multiple_matches(self):
        self.assertEqual(kmp_search("AABAACAADAABAABA", "AABA"), [0, 9, 12])

    def test_no_match(self):
        self.assertEqual(kmp_search("HELLO WORLD", "PYTHON"), [])

    def test_overlapping_matches(self):
        self.assertEqual(kmp_search("AAAA", "AA"), [0, 1, 2])

    def test_empty_needle(self):
        self.assertEqual(kmp_search("SOMETHING", ""), [])

if __name__ == "__main__":
    unittest.main()