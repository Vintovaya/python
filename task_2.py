# Винтовая Дария 44-22-122 задание 2
import math
import sys
import unittest
def main(*args):
    try:
        x = float(args[0][1])
        if x < 0.5:
            return math.sqrt(math.sin(x) + math.cos(x) ** 2)
        else:
            return math.exp(x ** 3 * (math.sin(3*x)))
    except:
        return "Произошла ошибка"

class SolverOfASystemOfEquationsTestCase(unittest.TestCase):
    def test_le(self):
        res = main(['...', 0.5])
        self.assertEqual(res, 1.1327936896058604)

    def test_r(self):
        res = main(['...', 0.9])
        self.assertEqual(res, 1.3655536252741407)

    def test_error(self):
        res = main()
        self.assertEqual(res, "Произошла ошибка")