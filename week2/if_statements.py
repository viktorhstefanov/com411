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



print("Please enter the first number.")
first_number = int(input())
print("Please enter the second number.")
second_number = int(input())

if first_number < second_number:
    print("The first number is the smallest!")
elif second_number < first_number:
    print("The second number is the smallest!")
elif first_number == second_number:
    print("Both numbers are equal!")



print("Please enter the first whole number.")
first = int(input())
print("Please enter the second whole number.")
second = int(input())
print("Please enter the third whole number")
third = int(input())

even = 0
odd = 0

if first % 2 == 0:
    even += 1
else:
    odd += 1

if second % 2 == 0:
    even += 1
else:
    odd += 1

if third % 2 == 0:
    even += 1
else:
    odd += 1

print(f"There were {even} even and {odd} odd numbers.")