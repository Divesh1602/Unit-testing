"""
Testing1.py: A module for testing the 'execute'
function in the question_1 module.
"""
import unittest
from question_1 import execute as exe


def is_int(variable):
    """Check if a variable is an integer."""
    return isinstance(variable, int)


class Testing1(unittest.TestCase):
    """
    Test cases for the 'execute' function in the question_1 module.
    """
    data_dict = exe()

    def test_check_datatype(self):
        """
        Test that keys and values in data_dict are of integer data type.
        """
        for key, value in self.data_dict.items():
            self.assertTrue(
                is_int(key),
                f"key: '{key}' should be of int datatype"
            )
            self.assertTrue(
                is_int(value),
                f"value: '{value}' should be of int datatype"
            )

    def test_check_size(self):
        """
        Test that the number of keys in data_dict is less than or equal to 10.
        """
        length = len(self.data_dict.keys())
        self.assertLessEqual(
            length, 10,
            "The data is from 2008-2017,"
            " but you have more than 10 years"
            " in your dict. Please check your code.")


if __name__ == '__main__':
    unittest.main()
