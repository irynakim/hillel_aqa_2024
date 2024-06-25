import unittest

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from homeworks import add_numbers


class AddNumbersPositiveTest(unittest.TestCase):

    def test_add_numbers_one_plus_one(self):
        expected_result = 2
        input_param_1 = 1
        input_param_2 = 1
        self.assertEqual(add_numbers(input_param_1, input_param_2), expected_result)

    def test_add_numbers_0_plus_0(self):
        expected_result = 0
        input_param_1 = 0
        input_param_2 = 0
        self.assertEqual(add_numbers(input_param_1, input_param_2), expected_result)

    def test_add_numbers_sum_0(self):
        expected_result = 0
        input_param_1 = -1
        input_param_2 = 1
        self.assertEqual(add_numbers(input_param_1, input_param_2), expected_result)


if __name__ == '__main__':
    unittest.main()
