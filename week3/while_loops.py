# Activity 1:
print("How many apples should I remove?")
apple = int(input())
apple_remove = 0

while apple_remove < apple:
    print("Removed apple.")
    apple_remove = apple_remove + 1

# Activity 2:
print("How many obstacles must I avoid?")
obstacle = int(input())
obstacle_number = 0

while obstacle_number < obstacle:
    obstacle_number = obstacle_number + 1
    print(f"Avoiding...Done {obstacle_number} obstacles avoided!")

print()
print("All obstacles avoided!")

# Activity 3:
print("How many bars should be charged?")
bars = int(input())
bars_charged = 0

while bars_charged < bars:
    bars_charged = bars_charged + 1
    print("Charging:", '█ ' * bars_charged )

print()
print("The battery is fully charged.")

# Activity 4:
print("Please enter a phrase")
