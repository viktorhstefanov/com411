# Activity 1:
print("Program started!")
print("Please enter a standard character:")
word = input()
if len(word) == 1:
    value = ord(word)
print(f"The ASCII code for {word} is {value}.")
print("Program Ended!")

# Activity 2
print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())

if code in range(32, 126):
    char = chr(code)
print(f"The character represented by the ASCII {code} is {char}.")
print("Program Ended!")
