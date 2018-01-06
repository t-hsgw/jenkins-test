import unittest
import sys
sys.path.append('../')
from main import *

class TestMain(unittest.TestCase):
    def test_sum(self):
        expected = 3
        actual = Main.sum(1, 2)
        self.assertEqual(expected, actual)

if __name__== '__main__':
    unittest.main()

