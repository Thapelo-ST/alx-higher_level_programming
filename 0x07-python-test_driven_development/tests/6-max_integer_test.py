#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        result = max_integer([-4, -2, -1, -3])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([1, -2, 3, -4])
        self.assertEqual(result, 3)

    def test_duplicate_numbers(self):
        result = max_integer([2, 2, 2, 2])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
