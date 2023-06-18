# Алдохина Элеонора Алексеевна, группа 44-22-121, вариант 2
import unittest
import math

def calculate_function2(x):
    if x < 0.1:
        result = math.sqrt(x) + x ** 2
    else:
        result = math.sin(x) + math.cos(x)
    return result

class TestFunction2(unittest.TestCase):
    def test_case1(self):
        result = calculate_function2(0)
        self.assertAlmostEqual(result, 0, places=7)

    def test_case2(self):
        result = calculate_function2(1)
        self.assertAlmostEqual(result, 1.3817732907, places=7)

if __name__ == "__main__":
    unittest.main()
