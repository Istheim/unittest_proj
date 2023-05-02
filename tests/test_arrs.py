import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)
        self.assertEqual(arrs.get([1, 2, 3], -1), 3)
        self.assertEqual(arrs.get([1, 2, 3], 3, 'default'), 'default')
        self.assertEqual(arrs.get([], 0, 'default'), 'default')
        self.assertEqual(arrs.get([1, 2, 3], -4, 'default'), 'default')

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1), [2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], end=3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3), [2, 3, 4])


if __name__ == '__main__':
    unittest.main()



