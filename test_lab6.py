import unittest
from lab6 import get_min_beers

class TestBeerParty(unittest.TestCase):
    
    def test_example_1(self):
        result = get_min_beers(2, 2, "YNNY")
        self.assertEqual(result, 2)

    def test_example_2(self):
        likes_str = "YNNYNYYNYNYYNYYNYN"
        result = get_min_beers(6, 3, likes_str)
        self.assertEqual(result, 2)
        
    def test_all_like_same_beer(self):
        likes_str = "YNNYNNYNN"
        result = get_min_beers(3, 3, likes_str)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
