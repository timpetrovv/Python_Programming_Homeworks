# Reading input
group_size = int(input())
season = input()

# Initializing base price per person
price_per_person = 0

# Calculating base price per person based on group size and season
if group_size <= 5:
    if season == "spring":
        price_per_person = 50.00
    elif season == "summer":
        price_per_person = 48.50
    elif season == "autumn":
        price_per_person = 60.00
    elif season == "winter":
        price_per_person = 86.00
else:
    if season == "spring":
        price_per_person = 48.00
    elif season == "summer":
        price_per_person = 45.00
    elif season == "autumn":
        price_per_person = 49.50
    elif season == "winter":
        price_per_person = 85.00

# Applying discount depending on the season:
#  15% discount for summer
if season == "summer":
    price_per_person *= 0.85
elif season == "winter": #, 8% Increase for winter
    price_per_person *= 1.08

# Calculating total price for the group
total_price = group_size * price_per_person

# Printing the result
print(f"{total_price:.2f} leva.")