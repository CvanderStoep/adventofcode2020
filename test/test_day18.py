import os
import unittest


from day18 import evaluate, evaluate2


TEST_DIRECTORY = os.path.dirname(__file__)


class TestDay18(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(7, evaluate('3 + 4'))
        self.assertEqual(16, evaluate('3 * 5 + 1'))

    def test_part_two(self):
        self.assertEqual(7, evaluate2('3 + 4'))
        self.assertEqual(18, evaluate2('3 * 5 + 1'))


if __name__ == '__main__':
    unittest.main()
