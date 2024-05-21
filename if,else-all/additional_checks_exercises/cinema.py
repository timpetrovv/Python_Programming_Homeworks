type_movie = input()
rows = int(input())
colums = int(input())

price = 0

if type_movie == "Premiere":
    price = (colums * rows) * 12.00
elif type_movie == "Normal":
    price = (colums * rows) * 07.50
elif type_movie == "Discount":
    price = (colums * rows) * 5.00
print(f"{price:.2f} leva")