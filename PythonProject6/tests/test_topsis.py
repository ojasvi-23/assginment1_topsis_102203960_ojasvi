import unittest
from topsis import topsis


class TestTopsis(unittest.TestCase):

    def test_topsis_function(self):
        data = [
            [250, 16, 12, 5],
            [200, 16, 8, 3],
            [300, 32, 16, 4],
            [275, 32, 8, 4]
        ]
        weights = [1, 1, 1, 1]
        impacts = ['+', '+', '-', '+']
        result = topsis(data, weights, impacts)
        expected_result = [0.56, 0.32, 0.78, 0.45]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

