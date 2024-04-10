import unittest
from sorting.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(merge_sort([5]), [5])

    def test_two_element_list(self):
        self.assertEqual(merge_sort([5, 3]), [3, 5])

    def test_multiple_element_list(self):
        self.assertEqual(merge_sort([5, 3, 8, 4, 2, 9, 1]), [1, 2, 3, 4, 5, 8, 9])

    def test_duplicate_elements_list(self):
        self.assertEqual(merge_sort([5, 3, 8, 4, 2, 9, 1, 5, 3]), [1, 2, 3, 3, 4, 5, 5, 8, 9])

    def test_negative_elements_list(self):
        self.assertEqual(merge_sort([5, -3, 8, 4, -2, 9, 1]), [-3, -2, 1, 4, 5, 8, 9])


if __name__ == '__main__':
    unittest.main()
