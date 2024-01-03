class BurndownSummaryItemDTO:
    
    story_points = 0

    def __init__(self, datetime, event_description):
        self.datetime = datetime
        self.event_description = event_description

    