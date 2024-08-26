import unittest
from calc import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculate("+", 2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = calculate("-", 5, 2)
        self.assertEqual(result, 3)

    def test_multiplication(self):
        result = calculate("*", 4, 3)
        self.assertEqual(result, 12)

    def test_division(self):
        result = calculate("/", 8, 2)
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate("/", 5, 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate("?", 2, 3)

if __name__ == '__main__':
    unittest.main()