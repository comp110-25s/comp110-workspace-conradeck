"""River Simulation: Fish Class"""

__author__ = "730830842"

"""File to define Fish class."""


class Fish:

    def __init__(self):
        """Initialize fish with age 0"""
        self.age = 0

    def one_day(self):
        """Age fish by 1 day"""
        self.age += 1
