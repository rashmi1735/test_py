import unittest


class TestSum(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum2(self):
        self.assertEqual(sum([2, 3, 4]), 9, "Should be 9")
        
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()
