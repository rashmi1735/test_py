import unittest
import sys
sys.path.append('../')
from src.code import sum,sum_only_positive

class TestSum(unittest.TestCase):

#     def test_sum1(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum2(self):
#         self.assertEqual(sum([2, 3, 4]), 8, "Should be 9")
        
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

    def test_sum(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_positive_ok(self):
        self.assertEqual(sum_only_positive(2, 2), 4)

    def test_sum_positive_fail(self):
        self.assertEqual(sum_only_positive(-1, 2), None)

if __name__ == '__main__':
    unittest.main()
