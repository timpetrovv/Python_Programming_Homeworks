budget = int(input())
season = input()
number_fisherman = int(input())
rent_ship = 0

if season == "Spring":
    if number_fisherman <= 6:
        rent_ship = 3000 * 0.90
    if 7 < number_fisherman <= 11:
        rent_ship = 3000 * 0.85
    if number_fisherman > 12:
        rent_ship = 3000 * 0.75
if season == "Summer":
    if number_fisherman <= 6:
        rent_ship = 4200 * 0.90
    if 7 < number_fisherman <= 11:
        rent_ship = 4200 * 0.85
    if number_fisherman > 12:
        rent_ship = 4200 * 0.75
if season == "Autumn":
    if number_fisherman <= 6:
        rent_ship = 4200 * 0.90
    if 7 < number_fisherman <= 11:
        rent_ship = 4200 * 0.85
    if number_fisherman > 12:
        rent_ship = 4200 * 0.75
if season == "Winter":
    if number_fisherman <= 6:
        rent_ship = 2600 * 0.90
    if 7 < number_fisherman <= 11:
        rent_ship = 2600 * 0.85
    if number_fisherman > 12:
        rent_ship = 2600 * 0.75

if number_fisherman % 2 == 0 and season != "Autumn":
    rent_ship *= 0.95

if budget >= rent_ship:
    money_left = budget - rent_ship
    print(f"Yes! You have {money_left:.2f} leva left.")
elif rent_ship > budget:
    money_needed = rent_ship - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")

