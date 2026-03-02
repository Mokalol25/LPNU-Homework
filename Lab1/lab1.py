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