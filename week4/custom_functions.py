# Activity 1:
def listen():
    print("What sound did you hear?")
    sound = input()
    print(f"That was a loud {sound}!")


listen()


# Activity 2:
def identify():
    print("What lies before us?")
    object = input()
    if object == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")


identify()


# Activity 3:
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")  #


# Activity 4:
def cross_bridge(step):
    for step in range(step):
        print("Crossed step!")
    if step > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


cross_bridge(3)
cross_bridge(6)


# Activity 5:
def climb_ladder(rem, cross):
    if rem > cross:
        print("Still some way to go!")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)
