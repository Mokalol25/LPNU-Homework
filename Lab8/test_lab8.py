import unittest
from lab8 import solve_ijones

class TestIJones(unittest.TestCase):

    def test_example_1(self):
        W, H = 3, 3
        grid = [
            "aaa",
            "cab",
            "def"
        ]
        result = solve_ijones(W, H, grid)
        print(f"\n--Розмір: {W}x{H}")
        print("Карта:")
        for row in grid:
            print(row)
        print(f"- Знайдено шляхів: {result}")
        self.assertEqual(result, 5)

    def test_example_2(self):
        W, H = 10, 1
        grid = [
            "abcdefaghi"
        ]
        result = solve_ijones(W, H, grid)
        print(f"\n--Розмір: {W}x{H}")
        print("Карта:")
        for row in grid:
            print(row)
        print(f"- Знайдено шляхів: {result}")
        self.assertEqual(result, 2)

    def test_example_3(self):
        W, H = 7, 6
        grid = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa"
        ]
        result = solve_ijones(W, H, grid)
        print(f"\n--Розмір: {W}x{H}")
        print("Карта:")
        for row in grid:
            print(row)
        print(f"- Знайдено шляхів: {result}")
        self.assertEqual(result, 201684)

    def test_single_cell(self):
        W, H = 1, 1
        grid = ["a"]
        result = solve_ijones(W, H, grid)
        print(f"\n--Розмір: {W}x{H}")
        print("Карта:")
        for row in grid:
            print(row)
        print(f"- Знайдено шляхів: {result}")
        self.assertEqual(result, 1)

    def test_no_jumps_possible(self):
        W, H = 3, 2
        grid = [
            "abc",
            "def"
        ]
        result = solve_ijones(W, H, grid)
        print(f"\n--Розмір: {W}x{H}")
        print("Карта:")
        for row in grid:
            print(row)
        print(f"- Знайдено шляхів: {result}")
        self.assertEqual(result, 2)

if __name__ == "__main__":
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIJones)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)