pen_count = int(input())
markers_count = int(input())
liters_board_cleaner = int(input())
discount_percentage = int(input())

Pen_price = pen_count * 5.80
markers_price = markers_count * 7.20
liters_board_price = liters_board_cleaner * 1.20

discount_value = discount_percentage / 100

total_price = (Pen_price + markers_price + liters_board_price)

price_discount = total_price - (total_price * discount_value)
print(price_discount)