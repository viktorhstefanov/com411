# Ask user to enter their name
#print("What is your name")
#name = input()
#print (f"It is nice to meet you {name}")

#print("Please enter a character for the eye")
#eye = input()
#print("##########")
#print(f"# {eye}    {eye} #")
#print("#        #")
#print("##########")

print("What is your name?")
firstname = input()


print("How old are you (in years)?")
age = input()

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = int(input())


bmi = weight / height ** 2
bmi_r = round(bmi, 2)


print(f"{firstname} your bmi is {bmi_r}.")




