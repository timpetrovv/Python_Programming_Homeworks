# User Input
age_input = float(input())
gender_input = input()

# Code logic

if age_input >= 16 and gender_input == "m":
    print("Mr.")
elif age_input < 16 and gender_input == "m":
    print("Master")
elif age_input >= 16 and gender_input == "f":
    print("Ms.")
elif age_input < 16 and gender_input == "f":
    print("Miss")