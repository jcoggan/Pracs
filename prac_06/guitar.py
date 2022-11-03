"""
Estimated time: 40min
Actual time: 60
Start time: 10:40am
Finished time: 11:52
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Not sure"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """gets age of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """determines if guitar is vintage"""
        if self.get_age() >= VINTAGE_AGE:
            return True
        return False
