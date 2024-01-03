import unittest
from Utilities.JiraBurndownUtilities import *

class TestRemoveStringsByIndex(unittest.TestCase):
    def test_remove_strings_remove_from_middle(self):
        # Test case 1: Normal case
        collection = ["a", "b", "c", "d", "e"]
        start_index = 1
        end_index = 2
        expected_output = ["a", "d", "e"]
        remove_strings_by_index(collection, start_index, end_index)
        self.assertEqual(collection, expected_output)

    def test_remove_strings_out_of_bounds_not_removed_and_no_error_raised(self):

        # Test case 2: No strings to remove
        collection = ["a", "b", "c"]
        start_index = -1
        end_index = -1
        expected_output = ["a", "b", "c"]
        remove_strings_by_index(collection, start_index, end_index)
        self.assertEqual(collection, expected_output)

    def test_remove_all_strings_returns_empty_collection(self):
        # Test case 3: All strings to remove
        collection = ["a", "b", "c"]
        start_index = 0
        end_index = 2
        expected_output = []
        remove_strings_by_index(collection, start_index, end_index)
        self.assertEqual(collection, expected_output)

if __name__ == '__main__':
    unittest.main()