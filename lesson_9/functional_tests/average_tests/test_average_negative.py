import unittest

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from homeworks import average


class AverageNegativeTest(unittest.TestCase):

    def test_average_input_string(self):
        expected_message = "unsupported operand type(s) for +: 'int' and 'str'"
        input_param = 'asd'

        with self.assertRaises(TypeError) as error:
            average(input_param)

        res = error.exception
        error_message = res.args[0]

        self.assertEqual(error_message, expected_message)

    def test_average_input_list(self):
        expected_message = 'division by zero'
        input_param = []

        with self.assertRaises(ZeroDivisionError) as error:  # with open(path) as f: f.read()
            # factorial(5)    # raise AsserationError
            average(input_param)

        res = error.exception
        error_message = res.args[0]

        self.assertEqual(error_message, expected_message)

if __name__ == '__main__':
    unittest.main()
