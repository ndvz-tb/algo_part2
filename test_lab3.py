import unittest
from lab3 import BinaryTree, is_tree_balanced

class TestBinaryTreeBalance(unittest.TestCase):

    def test_balanced_tree_from_image(self):
        """Тест дерева з умови задачі"""
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertTrue(is_tree_balanced(root))

    def test_balanced_tree_simple(self):
        """Тест простого збалансованого дерева"""
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree_left_heavy(self):
        """Тест незбалансованого дерева (вліво)"""  
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        self.assertFalse(is_tree_balanced(root))

    def test_unbalanced_tree_right_heavy(self):
        """Тест незбалансованого дерева (вправо)"""
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.right.right = BinaryTree(3)
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        """Порожнє дерево вважається збалансованим"""
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        """Дерево з одного кореня вважається збалансованим"""
        root = BinaryTree(1)
        self.assertTrue(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()