import os

class BinaryTree:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.__root = None

    def build_from_file(self, filename="tree.txt"):
        """Будує дерево з файлу із захистом від некоректних даних"""
        
        if not filename.endswith('.txt'):
            print(f"Файл '{filename}' має неправильний формат. Потрібен .txt")
            return False
            
        if not os.path.exists(filename):
            print(f"Файл '{filename}' не знайдено")
            return False

        max_size_bytes = 1024 * 1024 
        if os.path.getsize(filename) > max_size_bytes:
            print(f"Файл '{filename}' великий")
            return False

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                vals = f.read().split()
        except Exception as e:
            print(f"Помилка при читанні файлу: {e}")
            return False
            
        if not vals or vals[0].lower() in ['null', 'nil', 'none']:
            return False
            
        try:
            self.__root = self.__Node(int(vals[0]))
        except ValueError:
            print(f"Корінь дерева '{vals[0]}' не є числом")
            return False

        queue = [self.__root]
        i = 1
        
        while queue and i < len(vals):
            curr = queue.pop(0)
            
            if i < len(vals):
                val_str = vals[i].lower()
                if val_str not in ['null', 'nil', 'none']:
                    try:
                        curr.left = self.__Node(int(vals[i]))
                        queue.append(curr.left)
                    except ValueError:
                        print(f"'{vals[i]}' не є числом. Пропускаємо вузол.")
                i += 1
                
            if i < len(vals):
                val_str = vals[i].lower()
                if val_str not in ['null', 'nil', 'none']:
                    try:
                        curr.right = self.__Node(int(vals[i]))
                        queue.append(curr.right)
                    except ValueError:
                        print(f"Попередження: '{vals[i]}' не є числом. Пропускаємо вузол.")
                i += 1
                
        return True

    def _check_height(self, node):
        if not node:
            return 0
        left_height = self._check_height(node.left)
        if left_height == -1: return -1
        right_height = self._check_height(node.right)
        if right_height == -1: return -1
        if abs(left_height - right_height) > 1: return -1 
        return max(left_height, right_height) + 1

    def is_balanced(self):
        return self._check_height(self.__root) != -1

    def display(self):
        if not self.__root:
            print("Дерево порожнє")
            return

        def get_h(node):
            if not node: return 0
            return max(get_h(node.left), get_h(node.right)) + 1
        
        h = get_h(self.__root)
        col_width = 7 
        width = (2**h) * col_width
        matrix = [[" " for _ in range(width)] for _ in range(h * 2)]
        
        def place(r, c, txt):
            s = str(txt)
            start_c = c - len(s) // 2
            for i, char in enumerate(s):
                if 0 <= start_c + i < width:
                    matrix[r][start_c + i] = char

        def fill(node, r, c, curr_h):
            if not node:
                place(r, c, "nil")
                return
            place(r, c, node.value)
            if curr_h > 1:
                step = int(2**(curr_h - 2) * 2)
                matrix[r+1][c - step//2] = "/"
                fill(node.left, r+2, c - step, curr_h-1)
                matrix[r+1][c + step//2] = "\\"
                fill(node.right, r+2, c + step, curr_h-1)
                
        fill(self.__root, 0, width // 4, h)
        
        for row in matrix:
            line = "".join(row).rstrip()
            if line:
                print(line)

if __name__ == "__main__":
    tree = BinaryTree()
    
    if tree.build_from_file("tree.txt"):
        tree.display() 
        print("Чи збалансоване дерево?:", tree.is_balanced())