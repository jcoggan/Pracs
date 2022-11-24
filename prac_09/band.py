class Band:
    """Band Class"""

    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, member):
        """Adds a member to the band"""
        self.members.append(member)

    def __str__(self):
        return f"{self.name} ({self.members})"

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument for all band members."""
        for member in self.members:
            print(f"{member.play()}")
