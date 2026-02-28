class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(node: BinaryTree) -> bool:
    """
    Перевіряє, чи є бінарне дерево збалансованим.
    """
    def check_height(current_node: BinaryTree) -> int:
        if current_node is None:
            return 0
        
        left_height = check_height(current_node.left)
        if left_height == -1:
            return -1
            
        right_height = check_height(current_node.right)
        if right_height == -1:
            return -1
            
        if abs(left_height - right_height) > 1:
            return -1
            
        return max(left_height, right_height) + 1

    return check_height(node) != -1