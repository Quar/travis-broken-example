import unittest
from simplepy.factorial import *

class TestFactorial(unittest.TestCase):
    def test_fact(self):
        FACT_12 = 479_001_600
        res = fact(12)
        self.assertEqual(res, FACT_12)

if __name__ == "__main__":
    unittest.main()