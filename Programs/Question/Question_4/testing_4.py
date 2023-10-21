"""
Testing4.py: A module for testing the 'execute'
function in the question_4 module.
"""
import unittest
from question_4 import execute as exe


def is_float(variable):
    """Check if a variable is an Float."""
    return isinstance(variable, float)


def is_str(variable):
    """Check if a variable is an integer."""
    return isinstance(variable, str)


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
                is_str(key),
                f"key: '{key}' should be of str datatype"
            )
            self.assertTrue(
                is_float(value[3]),
                f"value: '{value[3]}' should be of float datatype"
            )

    def test_check_size(self):
        """
        Test that the number of keys in data_dict is less than or equal to 10.
        """
        length = len(self.data_dict.keys())
        self.assertLessEqual(
            length, 11,
            "There are only 11 bowlers in the"
            " data of 2015 please check your code"
        )


if __name__ == '__main__':
    unittest.main()
