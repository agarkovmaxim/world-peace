# Лукьянчикова Анастасия Евгеньевна, группа 44-22-121, вариант 15
import unittest
import math

def calculate_function3(x):
    if x < 2:
        result = math.log(abs(x * math.sin(x)))
    else:
        result = math.sqrt(x + 7)
    return result

class TestFunction3(unittest.TestCase):
    def test_case1(self):
        result = calculate_function3(-1)
        self.assertAlmostEqual(result, -0.17260374626909167, places=7)

    def test_case2(self):
        result = calculate_function3(2)
        self.assertAlmostEqual(result, 3.0, places=7)

if __name__ == "__main__":
    unittest.main()
