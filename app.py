import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)  # Проверка сложения положительных чисел
        self.assertEqual(self.calculator.add(-2, 3), 1)  # Проверка сложения отрицательного и положительного числа
        self.assertEqual(self.calculator.add(-2, -3), -5)  # Проверка сложения двух отрицательных чисел

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)  # Проверка умножения положительных чисел
        self.assertEqual(self.calculator.multiply(-2, 3),
                         -6)  # Проверка умножения отрицательного и положительного числа
        self.assertEqual(self.calculator.multiply(-2, -3), 6)  # Проверка умножения двух отрицательных чисел
        self.assertEqual(self.calculator.multiply(0, 3), 0)  # Проверка умножения на ноль


if __name__ == '__main__':
    unittest.main()
