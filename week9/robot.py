class Robot:

    MAX_ENERGY = 0

    def __init__(self, name="Robot", age=0, energy=0):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"{self.name}, {self.age}, {self.energy}")

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old and energy is {self.energy}.'

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'


robot = Robot()
robot.display()