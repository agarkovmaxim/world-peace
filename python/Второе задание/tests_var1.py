# Агарков Максим Алексеевич, группа 44-22-121, вариант 1
import unittest
import math

def calculate_function1(x):
    if x > -1:
        result = x + 2 * x ** 2
    else:
        result = x * math.log(abs(x + 2))
    return result

class TestFunction1(unittest.TestCase):
    def test_case1(self):
        result = calculate_function1(0)
        self.assertEqual(result, 0)

    def test_case2(self):
        result = calculate_function1(-1)
        self.assertAlmostEqual(result, -0.0, places=7)

    def test_case3(self):
        result = calculate_function1(2)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
