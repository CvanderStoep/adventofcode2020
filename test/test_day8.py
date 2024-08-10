import os
import unittest


from day8 import compute_part_one, compute_part_two


TEST_DIRECTORY = os.path.dirname(__file__)


class TestDay8(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1262, compute_part_one(TEST_DIRECTORY + '/input/input8.txt'))

    def test_part_two(self):
        self.assertEqual(1643, compute_part_two(TEST_DIRECTORY + '/input/input8.txt'))


if __name__ == '__main__':
    unittest.main()
