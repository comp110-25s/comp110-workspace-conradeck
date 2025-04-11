"""River Simulation: Fish Class."""

__author__ = "730830842"


class Fish:
    """Fish in the river."""

    def __init__(self):
        """Initialize fish with age 0."""
        self.age = 0

    def one_day(self):
        """Age fish by 1 day."""
        self.age += 1
