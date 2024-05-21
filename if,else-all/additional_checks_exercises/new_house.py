flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0

if flowers == "Roses":
    if number_flowers > 80:
        price = number_flowers * (5 * 0.90)
    else:
        price = number_flowers * 5
elif flowers == "Dahlias":
    if number_flowers > 90:
        price = number_flowers * (3.80 * 0.85)
    else:
        price = number_flowers * 3.80
elif flowers == "Tulips":
    if number_flowers > 80:
        price = number_flowers * (2.80 * 0.85)
    else:
        price = number_flowers * 2.80
elif flowers == "Narcissus":
    if number_flowers < 120:
        price = number_flowers * (3 * 1.15)
    else:
        price = number_flowers * 3
elif flowers == "Gladiolus":
    if number_flowers < 80:
        price = number_flowers * (2.50 * 1.20)
    else:
        price = number_flowers * 2.5

if price > budget:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
elif budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number_flowers} {flowers} and {money_left:.2f} leva left.")
