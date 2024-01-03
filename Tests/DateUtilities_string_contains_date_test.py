import unittest
from Utilities.DateUtilities import *

class TestDataUtilities(unittest.TestCase):
    def test_line_containing_date_value_returns_true(self):
        line_of_text = "13/12/2023 3:12 PM	SBS-77863	Burndown	Issue completed"
        expected_result = True
        self.assertEqual(string_contains_date(line_of_text), expected_result)

    def test_line_containing_no_date_value_returns_false(self):
        line_of_text = "SBS-77863	Burndown	Issue completed"
        expected_result = False
        self.assertEqual(string_contains_date(line_of_text), expected_result)

if __name__ == '__main__':
    unittest.main()