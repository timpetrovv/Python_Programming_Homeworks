price_vacancy = float(input())

count_puzzles = float(input())
count_dolls = float(input())
count_teddybears = float(input())
count_mininos = float(input())
count_trucks = float(input())

discount = 0

#calcualte the price
puzzles = count_puzzles * 2.60
dolls = count_dolls * 3
teddybears = count_teddybears * 4.10
minions = count_mininos * 8.20
trucks = count_trucks * 2
# Price without discount:
price = puzzles + dolls + teddybears + trucks + minions


total_count_toys = count_puzzles + count_dolls + count_teddybears + count_mininos + count_trucks

discount = 0

if total_count_toys >= 50:
    discount = (price * 0.25)

total_price = price - discount

rent1 = total_price - (total_price * 0.1)
rent = total_price - rent1
win = total_price - rent

if win >= price_vacancy:
    plus = win - price_vacancy
    print(f"Yes! {plus:.2f} lv left.")
elif win < price_vacancy:
    minus = price_vacancy - win
    print(f'Not enough money! {minus:.2f} lv needed.')