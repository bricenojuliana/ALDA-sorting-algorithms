import unittest
from sorting import bubble_sort, merge_sort, quick_sort, insertion_sort, selection_sort


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.unsorted_list = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_list = [1, 2, 3, 4, 5, 6, 7]
        self.duplicates_list = [4, 2, 4, 3, 1, 2, 1]
        self.empty_list = []
        self.expected_sorted = [11, 12, 22, 25, 34, 64, 90]
        self.expected_sorted_duplicates = [1, 1, 2, 2, 3, 4, 4]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.unsorted_list[:]), self.expected_sorted)
        self.assertEqual(bubble_sort(self.sorted_list[:]), self.sorted_list)
        self.assertEqual(bubble_sort(self.duplicates_list[:]), self.expected_sorted_duplicates)
        self.assertEqual(bubble_sort(self.empty_list[:]), [])

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.unsorted_list[:]), self.expected_sorted)
        self.assertEqual(merge_sort(self.sorted_list[:]), self.sorted_list)
        self.assertEqual(merge_sort(self.duplicates_list[:]), self.expected_sorted_duplicates)
        self.assertEqual(merge_sort(self.empty_list[:]), [])

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.unsorted_list[:]), self.expected_sorted)
        self.assertEqual(quick_sort(self.sorted_list[:]), self.sorted_list)
        self.assertEqual(quick_sort(self.duplicates_list[:]), self.expected_sorted_duplicates)
        self.assertEqual(quick_sort(self.empty_list[:]), [])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.unsorted_list[:]), self.expected_sorted)
        self.assertEqual(insertion_sort(self.sorted_list[:]), self.sorted_list)
        self.assertEqual(insertion_sort(self.duplicates_list[:]), self.expected_sorted_duplicates)
        self.assertEqual(insertion_sort(self.empty_list[:]), [])

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.unsorted_list[:]), self.expected_sorted)
        self.assertEqual(selection_sort(self.sorted_list[:]), self.sorted_list)
        self.assertEqual(selection_sort(self.duplicates_list[:]), self.expected_sorted_duplicates)
        self.assertEqual(selection_sort(self.empty_list[:]), [])


if __name__ == "__main__":
    unittest.main()
