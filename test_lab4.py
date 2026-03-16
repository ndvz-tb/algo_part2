import unittest
from lab4 import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):
    def setUp(self):
        """Перед кожним тестом створюємо повністю чисту чергу, 
        щоб тести не змішувалися і не заважали один одному."""
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_peek(self):
        """Перевіряємо, чи програма реально бачить найважливіше завдання 
        після того, як ми закинули в неї кілька різних."""
        self.pq.insert("Завдання А", 10)
        self.pq.insert("Завдання Б", 50)
        self.pq.insert("Завдання В", 30)
        
        val, prio = self.pq.peek()
        self.assertEqual(val, "Завдання Б")
        self.assertEqual(prio, 50)

    def test_extract_max_order(self):
        """Кидаємо завдання впереміш і дивимось, чи видає їх черга 
        строго по черзі: від найважливішого до найменш важливого."""
        self.pq.insert("Низький", 10)
        self.pq.insert("Високий", 100)
        self.pq.insert("Середній", 50)

        self.assertEqual(self.pq.extract_max(), ("Високий", 100))
        self.assertEqual(self.pq.extract_max(), ("Середній", 50))
        self.assertEqual(self.pq.extract_max(), ("Низький", 10))
        
        self.assertIsNone(self.pq.extract_max())

    def test_empty_queue(self):
        """Дивимось, що буде, якщо спробувати дістати завдання з порожньої черги. 
        Програма не має вибивати помилку, а просто повернути нічого (None)."""
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.extract_max())

    def test_same_priority(self):
        """Підкидаємо програмі 'каверзний' випадок: два різні завдання 
        з абсолютно однаковим пріоритетом. Перевіряємо, чи вона не загубить жодне."""
        self.pq.insert("Завдання 1", 20)
        self.pq.insert("Завдання 2", 20)
        
        val1, prio1 = self.pq.extract_max()
        val2, prio2 = self.pq.extract_max()
        
        self.assertEqual(prio1, 20)
        self.assertEqual(prio2, 20)
        
        extracted = {val1, val2}
        self.assertEqual(extracted, {"Завдання 1", "Завдання 2"})

if __name__ == "__main__":
    unittest.main(verbosity=0)