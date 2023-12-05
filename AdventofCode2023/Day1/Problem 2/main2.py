import unittest
import re

def string_int(string):
    int_arr = []
    
    intt = re.findall(r'(oneight|twone|threight|fiveight|sevenine|eightwo|nineight|one|two|three|four|five|six|seven|eight|nine|[0-9])', string)
    numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,"seven":7, "eight":8, "nine":9,'1':1,'2':2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9, 'twone':(2,1), 'oneight':(1,8), 'threight':(3,8), 'fiveight':(5,8), 'sevenine':(7,9), 'nineight':(9,8),'eightwo':(8,2)}
    int_ = []
    intt = list(map(lambda x: numbers[x], intt))
    for i in intt:
        if type(i) == tuple:
            int_.extend(list(i))
        else:
            int_.append(i)
    return int_

def read_input(filename):
    ar2 = []
    file_reader = open(filename)
    for i in file_reader.readlines():
        ok = string_int(i)
        ar2.append(ok[0]*10 + ok[-1])
    file_reader.close()
    return sum(ar2)

class Unittest1(unittest.TestCase):
    def tests(self):
        self.assertEqual(string_int('1234'), [1,2,3,4])
        self.assertEqual(string_int('91212129'), [9,1,2,1,2,1,2,9])
        self.assertEqual(string_int('1abc2'), [1,2])
        self.assertEqual(string_int('pqr3stu8vwx'), [3,8])
        self.assertEqual(string_int('a1b2c3d4e5f'), [1,2,3,4,5])
        self.assertEqual(string_int('treb7uchet'), [7])
        self.assertEqual(string_int('two1nine'), [2,1,9])
        self.assertEqual(string_int('eightwothree'),[8,2,3])
        self.assertEqual(string_int('abcone2threexyz'), [1,2,3])
        self.assertEqual(string_int('xtwone3four'), [2,1,3,4])
        self.assertEqual(string_int('4nineeightseven2'), [4,9,8,7,2])
        self.assertEqual(string_int('zoneight234'), [1,8,2,3,4])
        self.assertEqual(string_int('7pqrstsixteen'), [7,6])
        self.assertEqual(read_input('AdventofCode2023/Day1/Problem 2/test2.txt'), 281)

if __name__ == '__main__':
    unittest.main(exit=False)
    print(read_input('AdventofCode2023/Day1/Problem 2/input.txt'))
