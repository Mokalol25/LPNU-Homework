import unittest
import sys
from lab6 import solve_gamsrv_with_capacity

class TestGamsrvCapacity(unittest.TestCase):

    def test_capacity_restriction(self):
        n, m = 6, 6
        clients = [1, 2, 6]
        edges = [
            (1, 3, 10), (3, 4, 80), (4, 5, 50),
            (5, 6, 20), (2, 3, 40), (2, 4, 100)
        ]
        capacities = {3: 5, 4: 1, 5: 5} 

        res = solve_gamsrv_with_capacity(n, m, clients, edges, capacities)
        
        print(f"\n--- Тест з обмеженням потужності ---")
        print(f"Нова мінімальна затримка: {res} ms (Вузол 4 проігноровано)")
        
        self.assertGreater(res, 100)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGamsrvCapacity)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=1).run(suite)