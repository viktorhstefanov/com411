# Activity 1
def directions():
    steps = []
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")
    print(steps)


def run_task1():
    directions()


run_task1()


# Activity 2
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    steps = movements()
    for step in range(0, len(steps), 2):
        print(f"{steps[step]} for {steps[step + 1]} steps")


run_task2()

