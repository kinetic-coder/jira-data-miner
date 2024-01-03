import unittest
from Utilities.JiraBurndownUtilities import *

class TestGetCommittedStoryPoints(unittest.TestCase):
    def test_collection_contains_numeric_story_points_returns_total(self):
        # Test case 1: Normal case
        jira_burndown_list = ["10", "1", "4"]
        expected_output = 15
        self.assertEqual(get_committed_story_points(jira_burndown_list), expected_output)

    def test_collection_is_empty_zero_story_points_returned(self):
        # Test case 2: No story points
        jira_burndown_list = []
        expected_output = 0
        self.assertEqual(get_committed_story_points(jira_burndown_list), expected_output)

    def test_collection_contains_numeric_story_points_returns_zero_story_points(self):
        # Test case 3: Multiple story points
        jira_burndown_list = ["Some data", "Sprint started by John Doe", "Story points:", "Story points"]
        expected_output = 0
        self.assertEqual(get_committed_story_points(jira_burndown_list), expected_output)

    def test_collection_contains_alpha_numerics_returns_zero_story_points(self):
        # Test case 3: Multiple story points
        jira_burndown_list = ["Some data", "2", "Story points:", "Story points"]
        expected_output = 0
        self.assertEqual(get_committed_story_points(jira_burndown_list), expected_output)

if __name__ == '__main__':
    unittest.main()