from inhabitant import Inhabitant


class Robot(Inhabitant):
    laws = "Protect, Obey and Survive"

    def __init__(self, name="Robot", age=0):
        super().__init__(name, age)

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old and energy is {self.energy}.'

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

    @staticmethod
    def the_laws():
        print(Robot.laws)
