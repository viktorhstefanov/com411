class Planet:

    def __init__(self, name):
        self.name = name
        self.humans = []
        self.robots = []

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    def __str__(self):
        return f"Planet {self.name} has the following humans: {self.humans} and robots: {self.robots}"

    def __repr__(self):
        return f"planet(name={self.name}, humans={self.humans}, robots={self.robots})"


