# User Input
animal_input = input()
animal_type = ""

# Logic
if animal_input == "dog" :
    animal_type = "mammal"
elif animal_input == "crocodile" :
    animal_type = "reptile"
elif animal_input == "tortoise":
    animal_type = "reptile"
elif animal_input == "snake":
    animal_type = "reptile"
else:
    animal_type = "unknown"

print(animal_type)
