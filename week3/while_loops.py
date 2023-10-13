print("How many apple should I remove")
apple = int(input())
apple_remove = 0

while apple_remove < apple:
    print("Removed apple.")
    apple_remove = apple_remove + 1


print("How many obstacles must I avoid?")
obstacle = int(input())
obstacle_number = 0

while obstacle_number < obstacle:
    obstacle_number = obstacle_number + 1
    print(f"Avoiding...Done {obstacle_number} obstacles avoided!")

print("All obstacles avoided!")