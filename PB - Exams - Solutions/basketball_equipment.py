annual_fee = int(input())

# Изчисления
basketball_shoes_price = 0.6 * annual_fee
basketball_outfit_price = 0.8 * basketball_shoes_price
basketball_ball_price = 0.25 * basketball_outfit_price
basketball_accessories_price = 0.2 * basketball_ball_price

# Обща цена
total_price = annual_fee + basketball_shoes_price + basketball_outfit_price + basketball_ball_price + basketball_accessories_price

# Изход
print(f'{total_price:.2f}')