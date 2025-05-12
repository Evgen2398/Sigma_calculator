# test_math_operations.py

import unittest
from sigma_calculator_lab2 import (
    calculate_sum,
    calculate_difference,
    calculate_product
)

class TestMathOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculate_sum([1, 2, 3]), 6)
        self.assertEqual(calculate_sum([]), 0)

    def test_difference(self):
        self.assertEqual(calculate_difference(10, 5), 5)

    def test_product(self):
        self.assertEqual(calculate_product([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()
