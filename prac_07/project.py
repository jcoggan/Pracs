class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}\t {self.start_date}\t {self.priority}\t" \
               f" {self.cost_estimate}\t {self.completion_percentage}"

    def is_complete(self):
        """determines if a projects' completion is at 100%"""
        if self.completion_percentage == 100:
            return True
        return False

    def __gt__(self, other):
        return self.priority > other.priority
