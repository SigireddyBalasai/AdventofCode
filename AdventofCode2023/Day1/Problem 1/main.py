import unittest
def string_int(string):
    int_arr = []
    for i in string:
        try:
            int_arr.append(int(i))
        except:
            pass
    final_int = int_arr[0]*10 + int_arr[-1]
    return final_int



def read_input(filename):
    ar2 = []
    file_reader = open(filename)
    for i in file_reader.readlines():
        ar2.append(string_int(i))
    file_reader.close()
    return sum(ar2)

        

from main import string_int
class CalibrationTestCase(unittest.TestCase):
    def test_recover_calibration_value(self):
        self.assertEqual(string_int('1234'), 14)
        self.assertEqual(string_int('91212129'), 99)
        self.assertEqual(string_int('1abc2'), 12)
        self.assertEqual(string_int('pqr3stu8vwx'), 38)
        self.assertEqual(string_int('a1b2c3d4e5f'), 15)
        self.assertEqual(string_int('treb7uchet'), 77)

class TestCase2(unittest.TestCase):
    def test_read_input(self):
        self.assertEqual(read_input('AdventofCode2023/Day1/Problem 1/test_input.txt'), 142)

if __name__ == '__main__':
    unittest.main(exit=False)
    print(read_input('AdventofCode2023/Day1/Problem 1/input.txt'))
