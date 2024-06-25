import unittest

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from homeworks import average


class AveragePositiveTest(unittest.TestCase):

    def test_average_1(self):
        expected_result = 3.5
        input_param = [1, 2, 3, 4, 5, 6]
        self.assertEqual(average(input_param), expected_result)


if __name__ == '__main__':
    unittest.main()
