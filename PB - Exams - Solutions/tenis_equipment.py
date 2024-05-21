import math

# Вход
racket_price = float(input())
racket_count = int(input())
shoes_count = int(input())

# Изчисляване на цената за ракетите, маратонките и останалата екипировка
racket_total_price = racket_price * racket_count
shoes_price = racket_price / 6
shoes_total_price = shoes_price * shoes_count
other_equipment_price = (racket_total_price + shoes_total_price) * 0.2

# Обща цена
total_price = racket_total_price + shoes_total_price + other_equipment_price

# Цена за Джокович
djokovic_price = total_price / 8

# Цена за спонсорите
sponsors_price = math.ceil(total_price * 7 / 8)

# Изход
print(f"Price to be paid by Djokovic {math.floor(djokovic_price)}")
print(f"Price to be paid by sponsors {sponsors_price}")