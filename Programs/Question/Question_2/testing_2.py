"""
Testing2.py: A module for testing the 'execute'
function in the question_2 module.
"""
import unittest
from question_2 import execute as exe


def is_int(variable):
    """Check if a variable is an integer."""
    return isinstance(variable, int)


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
        for key, value_data in self.data_dict.items():
            self.assertTrue(
                is_str(key),
                f"key: '{key}' should be of string datatype"
            )
            for key, value in value_data.items():
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
            length, 8,
            "There are only 8 teams please check your code"
        )


if __name__ == '__main__':
    unittest.main()
