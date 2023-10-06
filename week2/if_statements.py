print("What type of book is this?")
book = input()

if book == "adventure":
    print(f"I like {book} books")
    print()
    print("Finished reading book.")


print("Please enter the activity to be performed.")
activity = input()

if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")

print("Activity completed!")


print("Towards which direction should I go (up, down, left or right?)")
direction = input()

if direction == "up":
    print("I am moving in an upwards direction")
elif direction == "down":
    print("I am moving in a downwards direction")
elif direction == "left":
    print("I am moving to the left")
elif direction == "right":
    print("I am moving to the right")
else:
    print("I do not understand where to move")


print("Please enter a whole number")
number = input()
remainder = int(number) % 2

if remainder != 0:
    print(f"The number {number} is an odd number.")
elif remainder == 0:
    print(f"The number {number} is an even number.")