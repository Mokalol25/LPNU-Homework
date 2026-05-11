import unittest
from lab7 import get_mst_and_cost

class TestVeniceMST(unittest.TestCase):
    
    def test_basic_matrix(self):
        matrix = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]
        cost, edges = get_mst_and_cost(matrix)
        
        self.assertEqual(cost, 16)
        
        self.assertEqual(len(edges), 4)
        
        self.assertTrue((0, 1) in edges or (1, 0) in edges)

    def test_single_island(self):
        matrix = [[0]]
        cost, edges = get_mst_and_cost(matrix)
        self.assertEqual(cost, 0)
        self.assertEqual(len(edges), 0)
        
    def test_two_islands(self):
        matrix = [
            [0, 10], 
            [10, 0]
        ]
        cost, edges = get_mst_and_cost(matrix)
        self.assertEqual(cost, 10)
        self.assertEqual(len(edges), 1)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)