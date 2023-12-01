from inhabitant import Inhabitant


class Human(Inhabitant):

    def __init__(self, name="Human", age=0):
        super().__init__(name, age)

    def __str__(self):
        return f'Human {self.name} is {self.age} years old and energy is {self.energy}.'

    def __repr__(self):
        return f'human(name={self.name}, age={self.age}, energy={self.energy}'
