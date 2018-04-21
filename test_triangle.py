import unittest
from lection3_Task7 import treangle_type

class TreangleTest(unittest.TestCase):
    def test_type(self):
        res = treangle_type(1,3,3)
        self.assertEqual(res, "equilateral")


if __name__ == "__main__":
    unittest.main()
