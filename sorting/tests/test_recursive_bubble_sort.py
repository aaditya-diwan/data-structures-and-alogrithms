import unittest
from sorting.recursive_bubble_sort import bubble_sort_recursive


class TestRecursiveBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        bubble_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        bubble_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        arr = [5, 3, 8, 4, 2, 5]
        bubble_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [2, 3, 4, 5, 5, 8])

    def test_empty_array(self):
        arr = []
        bubble_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [5]
        bubble_sort_recursive(arr, len(arr))
        self.assertEqual(arr, [5])


if __name__ == '__main__':
    unittest.main()