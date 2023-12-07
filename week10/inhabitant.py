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

    def grow(self):
        self.age += 1

    def eat(self, amount):
        replenish = self.energy + amount
        if replenish <= 100:
            self.energy = replenish
        elif replenish > 100:
            self.energy = 100

    def move(self, distance):
        movement = self.energy - distance
        if movement <= 0:
            self.energy = 0
        elif movement >= 0:
            self.energy = movement


