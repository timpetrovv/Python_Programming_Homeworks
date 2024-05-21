days = int(input())
room_type = input()
rating = input()

price_per_night = 0
days -= 1
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00


#print(f"Цена на вечер: {price_per_night}")
#print(f"Брой Дни: {days}")

total_price = days * price_per_night

#print(f"Total_price = {total_price}")

if days > 15 and room_type == "president apartment":
    total_price *= 0.8  # 20% discount
elif 10 <= days <= 15 and room_type == "president apartment":
    total_price *= 0.85  # 15% discount
elif days <= 10 and room_type == "president apartment":
    total_price *= 0.85  # 10% discount
elif days >= 15 and room_type == "apartment":
    total_price *= 0.5  # 50% discount
elif 10 <= days <= 15 and room_type == "apartment":
    total_price *= 0.65  # 35% discount
elif days < 10 and room_type == "apartment":
    total_price *= 0.7
elif days >= 15 and room_type == "room for one person":
    total_price *= 0.9  # 10% discount


if rating == "positive":
    total_price *= 1.25  # 25% increase
elif rating == "negative":
    total_price *= 0.9  # 10% decrease



print(f"{total_price:.2f}")



