from datetime import timedelta, date
from dateutil.parser import parse
import re

def get_date_range(start_date, end_date):
    # Ensure the start_date is less than or equal to end_date
    if start_date > end_date:
        raise ValueError("Start date must be less than or equal to end date")

    # Generate dates
    delta = end_date - start_date
    return [start_date + timedelta(days=i) for i in range(delta.days + 1)]

def string_contains_date(text_to_check):
    # This pattern matches dates in the format dd/mm/yyyy
    pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'

    match = re.search(pattern, text_to_check)
    
    return match is not None

def get_date_from_string(text_to_check):
    # This pattern matches dates in the format dd/mm/yyyy
    pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
    match = re.search(pattern, text_to_check)
    return match.group(0) if match else None