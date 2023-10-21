import unittest
import sys
sys.path.append("../Question")
from question_3 import execute as exe


def is_int(variable):
    return isinstance(variable, int)
def is_str(variable):
	return isinstance(variable,str)

class Testing1(unittest.TestCase):
	data_dict=exe()

	def test_check_datatype(self):
		for key,value in self.data_dict.items():
			self.assertTrue(is_str(key), f"key: '{key}' should be of string datatype")
			self.assertTrue(is_int(value), f"value: '{value}' should be of int datatype")	

	def test_check_size(self):
		length=len(self.data_dict.keys())
		self.assertLessEqual(length,3,"There are only 3 teams in the data of 2016 please check your code")

if __name__ == '__main__':
    unittest.main()


