import unittest
from math import add, multiply


class MathTests(unittest.TestCase):
    # test functions must start with keyword 'test'
    def test_add0(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add1(self):
        self.assertEqual(add(-2, 3), 1)

    def test_add2(self):
        self.assertNotEqual(add('hello', 'world'), 'helloworld')
        self.assertFalse(add('hello', 'world'))

    def test_multiply0(self):
        self.assertEqual(multiply(3,5), 15)

if __name__ == "__main__":
    unittest.main()