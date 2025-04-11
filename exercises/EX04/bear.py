"""River Simulation: Bear class"""

__author__ = "730830842"

"""File to define Bear class."""


class Bear:
    """A bear in the river ecosystem"""

    def __init__(self):
        """Initialize bear with age 0 and hunger 0"""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Age bear by 1 day and decrease hunger score"""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """increase hunger by fish eaten"""
        self.hunger_score += num_fish
