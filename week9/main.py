from planet import Planet
from human import Human

planet1 = Planet("Earth")

human1 = Human("Bob")

planet1.add_human(human1)

print(planet1.humans)