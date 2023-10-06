print("What type of adventure should I have?")
type = input()


if (type == "scary") or (type == "short"):
    print("Entering the dark forest!")
elif (type == "safe") or (type == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")

print("What did I hear?")
sound = input()
print("What did I see?")
object = input()

if (sound == "grrr") and (object == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue!")


