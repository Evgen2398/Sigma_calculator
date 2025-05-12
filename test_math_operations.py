# test_math_operations.py

import unittest
from math_operations import (
    calculate_sum,
    calculate_difference,
    calculate_product,
    calculate_division
)

class TestMathOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculate_sum([1, 2, 3]), 6)
        self.assertEqual(calculate_sum([]), 0)

    def test_difference(self):
        self.assertEqual(calculate_difference(10, 5), 5)

    def test_product(self):
        self.assertEqual(calculate_product([1, 2, 3]), 6)

    def test_division(self):
        self.assertEqual(calculate_division(10, 2), 5)
# 228
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate_division(10, 0)

if __name__ == '__main__':
    unittest.main()
