import unittest

def calculate_sum(numbers):
    return sum(numbers)

class TestCalculateSum(unittest.TestCase):

    def test_sum_of_positive_numbers(self):
        self.assertEqual(calculate_sum([1, 2, 3]), 6)

    def test_sum_with_negative_numbers(self):
        self.assertEqual(calculate_sum([-1, -2, 3]), 0)

    def test_sum_of_empty_list(self):
        self.assertEqual(calculate_sum([]), 0)

    def test_sum_of_single_element(self):
        self.assertEqual(calculate_sum([5]), 5)

    def test_sum_of_floats(self):
        self.assertAlmostEqual(calculate_sum([1.1, 2.2, 3.3]), 6.6)

if __name__ == '__main__':
    unittest.main()
