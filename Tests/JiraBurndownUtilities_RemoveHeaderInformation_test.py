import unittest
from Utilities.JiraBurndownUtilities import *

# Test cases for remove_header_information
class TestRemoveHeaderInformation(unittest.TestCase):

    def test_remove_from_middle_of_collection_returns_existing_strings(self):
        input_data = ["Skip to main contentSkip to sidebar", "Jira", "Sprint started by John Smith", "0", "40"]
        expected_output = ["0", "40"]
        self.assertEqual(remove_header_information(input_data, "Sprint started by"), expected_output)

if __name__ == '__main__':
    unittest.main()