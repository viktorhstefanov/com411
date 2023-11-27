class Planet:

    def __init__(self, name):
        self.name = name
        self.inhabitants = {
            "humans": [],
            "robots": []
        }

    def add_human(self, human):
        self.inhabitants["humans"].append(human)

    def remove_human(self, human):
        self.inhabitants["humans"].remove(human)

    def add_robot(self, robot):
        self.inhabitants["robots"].append(robot)

    def remove_robot(self, robot):
        self.inhabitants["robots"].remove(robot)

    def __str__(self):
        return f"Planet {self.name} has the following humans: {self.inhabitants['humans']} and robots: {self.inhabitants['robots']}"

    def __repr__(self):
        return f"planet(name={self.name}, humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"

