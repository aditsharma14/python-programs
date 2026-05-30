import unittest
from mymodule import sqaure, double
class TestMyModule(unittest.TestCase):
    def test_sqaure(self):
        self.assertEqual(sqaure(2), 4)
        self.assertEqual(sqaure(-3), 9)
        self.assertEqual(sqaure(0), 0)

    def test_double(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(-3), -6)
        self.assertEqual(double(0), 0)

if __name__ == '__main__':
    unittest.main()