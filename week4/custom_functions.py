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
escape_by("cross bridge ahead")