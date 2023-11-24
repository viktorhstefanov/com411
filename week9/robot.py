class Robot:

    MAX_ENERGY = 0

    def __init__(self, name="Robot", age=0, energy=0):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"{self.name}, {self.age}, {self.energy}")


robot = Robot()
robot.display()