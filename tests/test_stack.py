"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):
    def test_Node(self):
        node1 = Node(1, 2)
        self.assertEquals(node1.data, 1)
        self.assertEquals(node1.next_node, 2)


    def test_Stack(self):
        stack = Stack()
        stack.push('first')
        stack.push('second')
        self.assertEquals(stack.top.data, 'second')

    def test_pop(self):
        stack = Stack()
        stack.push('first')
        stack.push('second')
        stack.pop()
        self.assertEquals(stack.top.data, 'first')
        stack.pop()
        with self.assertRaises(AttributeError):
            stack.top.data


if __name__ == '__main__':
    unittest.main()
