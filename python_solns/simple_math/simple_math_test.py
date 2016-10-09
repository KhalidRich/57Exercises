# test for simple_math.py

import unittest
from simple_math import add, sub, multi, div

class SimpleMathTest(unittest.TestCase):
    def test_add(self):
        # test the add function
        self.assertEqual(add(1,0), 1)
        self.assertEqual(add(3,4), 7)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(-3, 5), 2)

    def test_sub(self):
        # test hte sub function
        self.assertEqual(sub(1,0), 1)
        self.assertEqual(sub(3,3), 0)
        self.assertEqual(sub(-3,3), -6)
        self.assertEqual(sub(3, -3), 6)

    def test_multi(self):
        #test the multi function
        self.assertEqual(multi(10, 1), 10)
        self.assertEqual(multi(10, 0), 0)
        self.assertEqual(multi(10, -1), -10)
        self.assertEqual(multi(-10, -1), 10)

    def test_div(self):
        #test the div function
        self.assertEqual(div(5,1), 5)
        self.assertEqual(div(5, -1), -5)
        self.assertEqual(div(-5, -1), 5)
        self.assertEqual(div(1485, 0), 'N/A')

if __name__ == "__main__":
    unittest.main()
