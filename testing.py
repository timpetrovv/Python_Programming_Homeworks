rose_price = 5
dalia_price = 3.8
lale_price = 2.8
narcis_price = 3
gladiolus_price = 2.5

flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0

if flowers == "Roses":
    if number_flowers > 80:
        price = number_flowers * (rose_price * 0.90)
    else:
        price = number_flowers * rose_price
elif flowers == "Dahlias":
    if number_flowers > 90:
        price = number_flowers * (dalia_price * 0.85)
    else:
        price = number_flowers * dalia_price
elif flowers == "Tulips":
    if number_flowers > 80:
        price = number_flowers * (lale_price * 0.85)
    else:
        price = number_flowers * lale_price
elif flowers == "Narcissus":
    if number_flowers < 120:
        price = number_flowers * (narcis_price * 1.15)
    else:
        price = number_flowers * narcis_price
elif flowers == "Gladiolus":
    if number_flowers < 80:
        price = number_flowers * (gladiolus_price * 1.20)
    else:
        price = number_flowers * gladiolus_price

if price > budget:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
elif budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number_flowers} {flowers} and {money_left:.2f} leva left.")