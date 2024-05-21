chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menu = float(input())

chicken_price = chicken_menus * 10.35
fish_price = fish_menus * 12.40
vegetarian_price = vegetarian_menu * 8.15

menus_total = chicken_price + fish_price + vegetarian_price

desert = menus_total * 20 / 100

delivery_fee = 2.50

total_price = menus_total + desert + delivery_fee
print(float(total_price))