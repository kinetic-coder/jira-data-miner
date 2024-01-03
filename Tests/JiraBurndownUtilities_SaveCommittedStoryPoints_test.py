import unittest
from Utilities.JiraBurndownUtilities import *

class TestSaveCommittedStoryPoints(unittest.TestCase):
    def test_save_committed_story_points_to_populated_data_range(self):
        collection = ["01/01/2024", "02/01/2024", "03/01/2024", "04/01/2024"]
        story_point_commitment = 40
        expected_output = ["01/01/2024, 40", "02/01/2024", "03/01/2024", "04/01/2024"]
        set_story_point_commitment(collection, story_point_commitment)
        self.assertEqual(collection, expected_output)
    
    def test_save_committed_story_points_to_empty_data_range_collection(self):
        collection = []
        story_point_commitment = 40
        expected_output = []
        set_story_point_commitment(collection, story_point_commitment)
        self.assertEqual(collection, expected_output)

    def test_save_committed_story_points_to_single_date_data_range_collection(self):
        collection = ["01/01/2024"]
        story_point_commitment = 40
        expected_output = ["01/01/2024, 40"]
        set_story_point_commitment(collection, story_point_commitment)
        self.assertEqual(collection, expected_output)

if __name__ == '__main__':
    unittest.main()