import unittest

def zigzag_matrix(m, n):
    matrix = [[0] * n for _ in range(m)]
    value = 1

    for s in range(m + n - 1):
        if s % 2 == 0:
            # рух вгору-вправо
            a = min(s, m - 1)
            b = s - a
            while a >= 0 and b < n:
                matrix[a][b] = value
                value += 1
                a -= 1
                b += 1
        else:
            # рух вниз-вліво
            b = min(s, n - 1)
            a = s - b
            while b >= 0 and a < m:
                matrix[a][b] = value
                value += 1
                a += 1
                b -= 1

    return matrix

class TestZigzagMatrix(unittest.TestCase):

    def check_matrix(self, m, n):
        matrix = zigzag_matrix(m, n)

        print(f"\nПеревірка для m={m}, n={n}")
        for a in matrix:
            print(a)

    def test_1(self):
        self.check_matrix(5, 5)

    def test_2(self):
        self.check_matrix(2, 4)

    def test_3(self):
        self.check_matrix(6, 1)

    def test_4(self):
        matrix = zigzag_matrix(1, 1)
        print("\nПеревірка для m=1, n=1")
        print(matrix)
        self.assertEqual(matrix, [[1]])

tester = TestZigzagMatrix()

tester.test_1()
tester.test_2()
tester.test_3()
tester.test_4()

unittest.main(verbosity=2, exit=False)