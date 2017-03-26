import unittest
import numpy as np

class TestPackage(unittest.TestCase):
    def test_dot_product(self):
        RES = 285
        a = np.array(range(10))
        res = np.dot(a, a)
        self.assertEqual(res, RES)

if __name__ == "__main__":
    unittest.main()