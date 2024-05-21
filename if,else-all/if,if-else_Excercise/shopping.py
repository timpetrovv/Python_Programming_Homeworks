budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

total_videocards = video_cards * 250


price_processors = total_videocards * 0.35
total_processors = price_processors * processors


price_ram_memory = total_videocards * 0.10
total_price_ram_memory = price_ram_memory * ram_memory

total_price = total_videocards + total_price_ram_memory + total_processors


if video_cards > processors:
    discount = 0.15 * total_price
    total_price -= discount

if budget >= total_price:
    left_money = budget - total_price
    print(f"You have {left_money:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")