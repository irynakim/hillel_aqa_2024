import unittest

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from homeworks import add_numbers


class AddNumbersNegativeTest(unittest.TestCase):  # test suite

    def test_add_numbers_input_string(self):
        expected_message = 'can only concatenate str (not "int") to str'
        input_param_1 = 'asd'
        input_param_2 = 1

        with self.assertRaises(TypeError) as error:
            add_numbers(input_param_1, input_param_2)

        res = error.exception
        error_message = res.args[0]

        self.assertEqual(error_message, expected_message)

    def test_add_numbers_input_list(self):
        expected_message = 'can only concatenate list (not "int") to list'
        input_param_1 = []
        input_param_2 = 1

        with self.assertRaises(TypeError) as error:  # with open(path) as f: f.read()
            # factorial(5)    # raise AsserationError
            add_numbers(input_param_1, input_param_2)

        res = error.exception
        error_message = res.args[0]

        self.assertEqual(error_message, expected_message)

    def test_add_numbers_input_None(self):
        expected_message = "unsupported operand type(s) for +: 'NoneType' and 'int'"
        input_param_1 = None
        input_param_2 = 1

        with self.assertRaises(TypeError) as error:
            add_numbers(input_param_1, input_param_2)

        error = error.exception
        error_message = error.args[0]

        self.assertEqual(error_message, expected_message)


if __name__ == '__main__':
    unittest.main()
