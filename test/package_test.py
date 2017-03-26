import unittest
import numpy as np
from simplepy import mysql
import os

CONFIG_FILE = "./test_config.yml"
cwd = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
cfg_file = os.path.join(cwd, CONFIG_FILE)


class TestPackage(unittest.TestCase):

    def test_dot_product(self):
        RES = 285
        a = np.array(range(10))
        res = np.dot(a, a)
        self.assertEqual(res, RES)

    def test_mysql(self):
        conn = mysql.get_conn(cfg_file)
        qry = """SELECT 2 + 3"""
        RES = pd.DataFrame({"SELECT 2 + 3":[5]})
        res = mysql.query(conn, qry)
        self.assertTrue(res.equals(RES))


if __name__ == "__main__":
    unittest.main()