import unittest
import sys
import os

# Ensure project root is importable
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root not in sys.path:
    sys.path.insert(0, root)

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_at_beginning_and_len(self):
        self.ll.insert_at_beginning(10)
        self.ll.insert_at_beginning(20)
        self.assertEqual(len(self.ll), 2)
        self.assertEqual(list(self.ll), [20, 10])

    def test_remove_at_beginning(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        removed = self.ll.remove_at_beginning()
        self.assertEqual(removed, 1)
        self.assertEqual(list(self.ll), [2])

    def test_remove_beginning_alias(self):
        self.ll.insert_at_end('a')
        self.assertEqual(self.ll.remove_beginning(), 'a')

    def test_insert_at_end_and_remove_at_end(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.ll.insert_at_end(3)
        self.assertEqual(list(self.ll), [1,2,3])
        removed = self.ll.remove_at_end()
        self.assertEqual(removed, 3)
        self.assertEqual(list(self.ll), [1,2])

    def test_insert_at_index(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(3)
        self.ll.insert_at(1, 2)
        self.assertEqual(list(self.ll), [1,2,3])

    def test_remove_at_index(self):
        for i in range(5):
            self.ll.insert_at_end(i)
        removed = self.ll.remove_at(2)
        self.assertEqual(removed, 2)
        self.assertEqual(list(self.ll), [0,1,3,4])

    def test_search(self):
        self.ll.insert_at_end('x')
        self.ll.insert_at_end('y')
        self.ll.insert_at_end('z')
        self.assertEqual(self.ll.search('y'), 1)
        self.assertEqual(self.ll.search('notfound'), -1)

    def test_remove_by_value(self):
        self.ll.insert_at_end('a')
        self.ll.insert_at_end('b')
        self.ll.insert_at_end('c')
        idx = self.ll.remove_by_value('b')
        self.assertEqual(idx, 1)
        self.assertEqual(list(self.ll), ['a','c'])

    def test_errors(self):
        with self.assertRaises(IndexError):
            self.ll.remove_at_beginning()
        with self.assertRaises(IndexError):
            self.ll.remove_at_end()
        with self.assertRaises(IndexError):
            self.ll.remove_at(0)
        with self.assertRaises(ValueError):
            self.ll.remove_by_value('nope')


if __name__ == '__main__':
    unittest.main()
