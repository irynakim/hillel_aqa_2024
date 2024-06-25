import unittest

from homeworks import add_numbers
from homeworks import average
from homeworks import sum_numbers


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


# CamelCase
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


class AveragePositiveTest(unittest.TestCase):

    def test_average_1(self):
        expected_result = 3.5
        input_param = [1, 2, 3, 4, 5, 6]
        self.assertEqual(average(input_param), expected_result)


class AverageNegativeTest(unittest.TestCase):

    def test_average_input_string(self):
        expected_message = "unsupported operand type(s) for +: 'int' and 'str'"
        input_param = 'asd'

        with self.assertRaises(TypeError) as error:
            average(input_param)

        res = error.exception
        pass
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


class Sum_NumbersPositiveTest(unittest.TestCase):

    def test_average_1(self):
        expected_result = 232
        input_param = [7, 5, 3, 2, 4, 6, 90, 8, 54, 35, 68, 65, 43, 33, 55]
        self.assertEqual(sum_numbers(input_param), expected_result)


if __name__ == '__main__':
    unittest.main()
