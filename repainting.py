nailone_needed_value = int(input())
paint_liters = int(input())
thinner_quantity = int(input())
Hours_work = int(input())

nailone_price = (nailone_needed_value + 2) * 1.50

# Calculate 10% of the paint.
paint_percentage = paint_liters * 10 / 100

paint_price = (paint_liters + paint_percentage) * 14.50

thinner_price = thinner_quantity * 5.00
plastic_bag = 0.40


# Total price for materials:
total_price = nailone_price + paint_price + thinner_price + plastic_bag

labour_per_hour = ( total_price * 30 / 100 ) * Hours_work

final_price = total_price + labour_per_hour
print(final_price)

