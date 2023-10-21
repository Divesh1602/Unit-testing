import unittest
import sys
sys.path.append("../Question")
from question_4 import execute as exe


def is_float(variable):
    return isinstance(variable, float)
def is_str(variable):
	return isinstance(variable,str)

class Testing1(unittest.TestCase):
	data_dict=exe()
	
	def test_check_datatype(self):
		for key,value in self.data_dict.items():
			self.assertTrue(is_str(key), f"key: '{key}' should be of string datatype")
			self.assertTrue(is_float(value[3]), f"value: '{value[3]}' should be of float datatype")	

	def test_check_size(self):
		length=len(self.data_dict.keys())
		self.assertLessEqual(length,11,"There are only 11 bowlers in the data of 2015 please check your code")

if __name__ == '__main__':
    unittest.main()


