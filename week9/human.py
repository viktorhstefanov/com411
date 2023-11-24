class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0,):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"{self.name}, {self.age}, {self.energy}")

    def __str__(self):
        return f'Human {self.name} is {self.age} years old and energy is {self.energy}.'

    def __repr__(self):
        return f'human(name={self.name}, age={self.age}, energy={self.energy}'

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



