degree = int(input())
time_day = input()
outfit = ""
shoes = ""

if 10 <= degree <= 18:
    if time_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degree <= 24:
    if time_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degree >= 25:
    if time_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")