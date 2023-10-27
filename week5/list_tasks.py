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


# Activity 3
def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        dire = direction[index]
        print(f"{index}: {dire}")
    user_input = input()
    if user_input == "0":
        return "Move Forward"
    elif user_input == "1":
        return "Move Backward"
    elif user_input == "2":
        return "Turn Left"
    elif user_input == "3":
        return "Turn Right"


def run_task4():
    route = []
    print("Working out an escape route.")
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


def run_task3():
    menu()


run_task3()

# Activity 4


run_task4()
