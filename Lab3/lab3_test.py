import unittest
from lab3 import BinaryTree, find_successor

class TestBinaryTreeSuccessor(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)

        self.root.left = BinaryTree(5, parent=self.root)
        self.root.left.left = BinaryTree(3, parent=self.root.left)
        self.node_7 = BinaryTree(7, parent=self.root.left)
        self.root.left.right = self.node_7
        
        self.root.right = BinaryTree(15, parent=self.root)
        self.node_20 = BinaryTree(20, parent=self.root.right)
        self.root.right.right = self.node_20
        self.node_12 = BinaryTree(12, parent=self.node_20)
        self.node_20.left = self.node_12

    def test_successor_7(self):
        print("\nПеревірка вузла 7")
        result = find_successor(self.node_7) 
        self.assertEqual(result.value, 10)
        print(f"Знайдено: {result.value}.")

    def test_successor_10(self):
        print("\nПеревірка вузла 10 (корінь)")
        result = find_successor(self.root) 
        self.assertEqual(result.value, 15)
        print(f"Знайдено: {result.value}.")

    def test_successor_15(self):
        print("\nПеревірка вузла 15")
        result = find_successor(self.root.right) 
        self.assertEqual(result.value, 12)
        print(f"Знайдено: {result.value}.")



if __name__ == "__main__":
    test_suite = TestBinaryTreeSuccessor()

    test_suite.setUp()
    
    test_suite.test_successor_7()
    test_suite.test_successor_10()
    test_suite.test_successor_15()
