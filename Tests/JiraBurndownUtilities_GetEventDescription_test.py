
import unittest
from Utilities.JiraBurndownUtilities import *

# Test cases for remove_header_information
class TestEventDescriptionRetried(unittest.TestCase):
    def test_from_string_with_instruction_returns_instruction(self):
        input_data = "13/12/2023 3:12 PM	SBS-77863	Burndown	Issue completed"
        expected_output = "Issue completed"
        self.assertEqual(get_event_description(input_data), expected_output)
    
    def test_from_string_without_instruction_returns_no_instruction(self):
        input_data = "13/12/2023 3:12 PM	SBS-77863	Burndown"
        expected_output = ""
        self.assertEqual(get_event_description(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()