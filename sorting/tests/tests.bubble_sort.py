import unittest
from sorting.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        self.assertEqual(bubble_sort([5, 3, 8, 4, 2, 5]), [2, 3, 4, 5, 5, 8])

    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(bubble_sort([5]), [5])

if __name__ == '__main__':
    unittest.main()