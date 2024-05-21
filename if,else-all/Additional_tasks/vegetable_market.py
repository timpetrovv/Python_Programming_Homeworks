price_vegetables = float(input())
price_fruits = float(input())
quantity_vegetables = int(input())
quantity_fruits = int(input())

total_vegetables = float(price_vegetables * quantity_vegetables)
print(total_vegetables)

total_fruits = float(price_fruits * quantity_fruits)
print(total_fruits)

Price_lv = total_fruits + total_vegetables

Total_eur = float(Price_lv / 1.94)
print("%.2f" % Total_eur)

