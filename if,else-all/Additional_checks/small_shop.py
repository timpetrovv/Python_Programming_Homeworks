product = input()
city = input()
quantity = float(input())


if city == "Sofia":
    if product == "coffee":
        price = 0.50 * quantity
    if product == "water":
        price = 0.80 * quantity
    if product == "beer":
        price = 1.20 * quantity
    if product == "sweets":
        price = 1.45 * quantity
    if product == "peanuts":
        price = 1.60 * quantity

if city == "Plovdiv":
    if product == "coffee":
        price = 0.40 * quantity
    if product == "water":
        price = 0.70 * quantity
    if product == "beer":
        price = 1.15 * quantity
    if product == "sweets":
        price = 1.30 * quantity
    if product == "peanuts":
        price = 1.50 * quantity

if city == "Varna":
    if product == "coffee":
        price = 0.45 * quantity
    if product == "water":
        price = 0.70 * quantity
    if product == "beer":
        price = 1.10 * quantity
    if product == "sweets":
        price = 1.35 * quantity
    if product == "peanuts":
        price = 1.55 * quantity

print(price)