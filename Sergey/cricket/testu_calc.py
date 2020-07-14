import unittest
import test_calc

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test_calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(test_calc.sub(4, 2), 2)

    def test_mul(self):
        self.assertEqual(test_calc.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(test_calc.div(8, 4), 2)

if __name__ == '__main__':
    unittest.main()
