from datetime import timedelta, date

def get_date_range(start_date, end_date):
    # Ensure the start_date is less than or equal to end_date
    if start_date > end_date:
        raise ValueError("Start date must be less than or equal to end date")

    # Generate dates
    delta = end_date - start_date
    return [start_date + timedelta(days=i) for i in range(delta.days + 1)]