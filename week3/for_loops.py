# Activity 1:
print("How many mountains should I display?")
mountains = int(input())

print("Displaying...")

for count in range(mountains):
    print("           __")
    print("          /  \_")
    print("         /^    \ ")
    print("        /  ^    \_")
    print("     _/ ^ ^     ^\ ")
    print("     /  ^     ^    \ ")

# Activity 2
print("How far are we from the target?")
step = int(input())

for count in range(step, 0, -1):
        print(f"{count} steps remaining")

print("Target achieved!")

