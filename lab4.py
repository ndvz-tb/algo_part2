class Node:
    """Клас, що представляє вузол червоно-чорного дерева."""
    
    def __init__(self, value, priority):
        """Ініціалізація вузла зі значенням, пріоритетом та початковим червоним кольором."""
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'RED'


class RedBlackPriorityQueue:
    """Черга з пріоритетами на основі червоно-чорного дерева."""
    
    def __init__(self):
        """Ініціалізація порожньої черги з обмежувальним чорним вузлом NIL."""
        self.NIL = Node(None, float('-inf'))
        self.NIL.color = 'BLACK'
        self.root = self.NIL

    def _left_rotate(self, x):
        """Виконує лівий поворот піддерева навколо заданого вузла x."""
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        """Виконує правий поворот піддерева навколо заданого вузла x."""
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _fix_insert(self, z):
        """Відновлює властивості червоно-чорного дерева після вставки нового вузла."""
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self._left_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = 'BLACK'

    def insert(self, value, priority):
        """
        Вставляє елемент у чергу. 
        За правилами: більший або рівний пріоритет йде у ліве піддерево, менший - у праве.
        """
        node = Node(value, priority)
        node.parent = self.NIL
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'RED'

        parent = self.NIL
        current = self.root
        
        while current != self.NIL:
            parent = current
            if priority >= current.priority:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent == self.NIL:
            self.root = node
        elif priority >= parent.priority:
            parent.left = node
        else:
            parent.right = node

        self._fix_insert(node)

    def _fix_delete(self, x):
        """Відновлює властивості червоно-чорного дерева після видалення чорного вузла."""
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def _transplant(self, u, v):
        """Замінює піддерево з коренем u на піддерево з коренем v."""
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def extract_max(self):
        """Видаляє та повертає елемент із найвищим пріоритетом (завжди крайній лівий вузол)."""
        if self.root == self.NIL:
            return None
        
        current = self.root
        while current.left != self.NIL:
            current = current.left
        max_node = current
        
        y = max_node
        y_color = y.color
        x = y.right 
        
        self._transplant(y, y.right)
        
        if y_color == 'BLACK':
            self._fix_delete(x)
        
        return max_node.value, max_node.priority

    def peek(self):
        """Повертає елемент із найвищим пріоритетом без його видалення з черги."""
        if self.root == self.NIL:
            return None
        
        current = self.root
        while current.left != self.NIL:
            current = current.left
        return current.value, current.priority

    def print_queue(self):
        """Простий метод для виводу черги на екран у рядок."""
        if self.root == self.NIL:
            print("Черга порожня")
            return
        
        print("Вміст черги: ", end="")
        self._print_inorder(self.root)
        print()

    def _print_inorder(self, node):
        """Класичний рекурсивний Inorder обхід (зліва направо)."""
        if node != self.NIL:
            self._print_inorder(node.left)
            print(f"[{node.value} (пріоритет {node.priority})]", end=" ")
            self._print_inorder(node.right)

    def get_min(self):
        if self.root == self.NIL:
            return None
        current = self.root
        while current.right != self.NIL:
            current = current.right
        return current.value, current.priority

    def clear(self):
        self.root = self.NIL


def main():
    todo_list = RedBlackPriorityQueue()
    
    while True:
        print("1 - Додати завдання")
        print("2 - Показати список")
        print("3 - Виконати найважливіше")
        print("4 - Знайти найменш важливе")
        print("5 - Очистити список")
        print("6 - Вийти")
        
        choice = input("Вибір: ")
        
        if choice == '1':
            try:
                priority = int(input("Пріоритет: "))
                task = input("Завдання: ")
                todo_list.insert(task, priority)
                print(f"Додано: {task} ({priority})")
            except ValueError:
                print("Пріоритет має бути числом")
                
        elif choice == '2':
            if todo_list.peek() is None:
                print("Список порожній")
            else:
                todo_list.print_queue()
                
        elif choice == '3':
            result = todo_list.extract_max()
            if result:
                task, priority = result
                print(f"Виконано: {task} ({priority})")
            else:
                print("Список порожній")
                
        elif choice == '4':
            result = todo_list.get_min()
            if result:
                print(f"Найменш важливе: {result[0]} ({result[1]})")
            else:
                print("Список порожній")
                
        elif choice == '5':
            todo_list.clear()
            print("Список очищено")
            
        elif choice == '6':
            break
            
        else:
            print("Невідома команда")

if __name__ == "__main__":
    main()