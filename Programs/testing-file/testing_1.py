import unittest
import sys
sys.path.append("../Question")
from question_1 import execute as exe


def is_int(variable):
    return isinstance(variable, int)


class Testing1(unittest.TestCase):
	data_dict=exe()
	def test_check_datatype(self):
		for key,value in self.data_dict.items():
			self.assertTrue(is_int(key), f"key: '{key}' should be of int datatype")
			self.assertTrue(is_int(value), f"value: '{value}' should be of int datatype")	

	def test_check_size(self):
		length=len(self.data_dict.keys())
		self.assertLessEqual(length,10,"The data is from 2008-2017 but you have more than 10 years in your dict please check your code")

if __name__ == '__main__':
    unittest.main()


