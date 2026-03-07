import unittest
from lab2 import max_hamsters


def total_food_used(k, hamsters):
    costs = []
    for H, G in hamsters:
        costs.append(H + G * (k - 1))
    costs.sort()
    return sum(costs[:k])


class TestHamsters(unittest.TestCase):

    def run_example(self, S, C, hamsters, expected, number):
        result = max_hamsters(S, C, hamsters)
        used_food = total_food_used(result, hamsters)

        print(f"\nПриклад {number}")
        print(f"Максимальна кількість хом'ячків: {result}")
        print(f"Вони з'їдають: {used_food} пакетів корму")
        print(f"Є в запасі: {S} пакетів корму")

        if used_food <= S:
            print(f"Залишиться корму: {S - used_food}")
            print("Усі обрані хом'ячки мають що їсти.")
        else:
            print(f"Не вистачає корму: {used_food - S}")
            print("Їжі недостатньо.")

        self.assertEqual(result, expected)

    def test_pryklad_1(self):
        self.run_example(
            S=7,
            C=3,
            hamsters=[[1, 2], [2, 2], [3, 1]],
            expected=2,
            number=1
        )

    def test_pryklad_2(self):
        self.run_example(
            S=19,
            C=4,
            hamsters=[[5, 0], [2, 2], [1, 4], [5, 1]],
            expected=3,
            number=2
        )

    def test_pryklad_3(self):
        self.run_example(
            S=3,
            C=2,
            hamsters=[[1, 50000], [1, 60000]],
            expected=1,
            number=3
        )
    def test_pryklad_4(self):
        self.run_example(
            S=32,
            C=3,
            hamsters=[[1, 2], [3, 4], [5, 6]],
            expected=2,
            number=4
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHamsters)
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)