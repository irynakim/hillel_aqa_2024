import unittest

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from homeworks import sum_numbers


class Sum_NumbersPositiveTest(unittest.TestCase):

    def test_average_1(self):
        expected_result = 232
        input_param = [7, 5, 3, 2, 4, 6, 90, 8, 54, 35, 68, 65, 43, 33, 55]
        self.assertEqual(sum_numbers(input_param), expected_result)


if __name__ == '__main__':
    unittest.main()
