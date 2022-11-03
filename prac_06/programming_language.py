"""
Estimated time: 20min
Actual time:32min
Start time: 10:00am
Finished time:10:32am
"""


class ProgrammingLanguage:
    """hi"""

    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Checks if typing is dynamic"""
        if self.typing == "Dynamic":
            return True
        return False

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
