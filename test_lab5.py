import unittest
from lab5 import get_min_knight_moves

class TestKnightMoves(unittest.TestCase):

    def test_same_position(self):
        self.assertEqual(get_min_knight_moves(8, (0, 0), (0, 0)), 0)

    def test_one_move(self):
        self.assertEqual(get_min_knight_moves(8, (0, 0), (2, 1)), 1)
        self.assertEqual(get_min_knight_moves(8, (0, 0), (1, 2)), 1)
        self.assertEqual(get_min_knight_moves(8, (3, 3), (4, 5)), 1)

    def test_corners(self):
        self.assertEqual(get_min_knight_moves(8, (0, 0), (7, 7)), 6)
        self.assertEqual(get_min_knight_moves(8, (7, 7), (0, 0)), 6)

    def test_adjacent_cell(self):
        self.assertEqual(get_min_knight_moves(8, (0, 0), (0, 1)), 3)

if __name__ == '__main__':
    unittest.main()