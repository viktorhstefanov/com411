class Inhabitant():
    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = Inhabitant.MAX_ENERGY

    def __str__(self):
        return f'Inhabitant {self.name} is {self.age} years old and energy is {self.energy}.'

    def __repr__(self):
        return f'inhabitant(name={self.name}, age={self.age}, energy={self.energy}'

    def display(self):
        print(f"""
       Name: {self.name}, 
       Age: {self.age}, 
       Energy: {self.energy}
""")


