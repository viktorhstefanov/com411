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

# Activity 3:
print("What level of brightness is required?")
brightness_level = int(input())
print("Adjusting brightness...")
print()

for count in range(2, brightness_level + 1, 2):
    print(f"Brightness level: ", {count * '*'})

print("Complete!")

# Activity 4
print("What word do you see?")
word = input()

print("Displaying input positions...")

for position in range(0, len(word), 1):
    print(f"index: {position}", end=" ")
    print(word[position])

print("Done!")
