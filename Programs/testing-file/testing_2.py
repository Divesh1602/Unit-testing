import unittest
import sys
sys.path.append("../Question")
from question_2 import execute as exe


def is_int(variable):
    return isinstance(variable, int)
def is_str(variable):
	return isinstance(variable,str)

class Testing1(unittest.TestCase):
	data_dict=exe()
	def test_check_datatype(self):
		for key,value_data in self.data_dict.items():
			self.assertTrue(is_str(key), f"key: '{key}' should be of string datatype")
			for key,value in value_data.items():
				self.assertTrue(is_int(key), f"key: '{key}' should be of int datatype")
				self.assertTrue(is_int(value), f"value: '{value}' should be of int datatype")

	def test_check_size(self):
		keys_length=len(self.data_dict.keys())
		self.assertLessEqual(keys_length,8,"There are only 8 teams please check your code")




if __name__ == '__main__':
    unittest.main()


