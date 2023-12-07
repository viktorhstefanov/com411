from inhabitant import Inhabitant
from human import Human
from robot import Robot


class Planet:

    inhabitants = None

    def __init__(self, name):
        self.name = name
        self.inhabitants = []

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def remove_inhabitant(self, inhabitant):
        self.inhabitants.remove(inhabitant)

    def __str__(self):
        return f"Planet {self.name} has the following inhabitants {self.inhabitants}"

    def __repr__(self):
        return f"planet(name={self.name}, inhabitants={self.inhabitants}"





