class BurndownSummaryItem:
    def __init__(self, date, story_points, story_point_progressions):
        self.date = date
        self.story_points = story_points
        self.story_points_progression = story_point_progressions

    def to_string(self):
        return f"{self.date}, {self.story_points}, {self.story_points_progression}"