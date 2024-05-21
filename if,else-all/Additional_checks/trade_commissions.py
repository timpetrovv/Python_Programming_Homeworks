# User Input
city = input()
sales_number = float(input())
price = ""
if_number_incorrect = True


if city == "Sofia":
    if 0 <= sales_number <= 500:
        price = sales_number * 0.05
    elif 500 < sales_number <= 1000:
        price = sales_number * 0.07
    elif 1000 < sales_number <= 10000:
        price = sales_number * 0.08
    elif sales_number > 10000:
        price = sales_number * 0.12
    else:
        if_number_incorrect = False
elif city == "Varna":
    if 0 <= sales_number <= 500:
        price = sales_number * 0.045
    elif 500 < sales_number <= 1000:
        price = sales_number * 0.075
    elif 1000 < sales_number <= 10000:
        price = sales_number * 0.1
    elif sales_number > 10000:
        price = sales_number * 0.13
    else:
        if_number_incorrect = False
elif city == "Plovdiv":
    if 0 <= sales_number <= 500:
        price = sales_number * 0.055
    elif 500 < sales_number <= 1000:
        price = sales_number * 0.08
    elif 1000 < sales_number <= 10000:
        price = sales_number * 0.12
    elif sales_number > 10000:
        price = sales_number * 0.145
    else:
        if_number_incorrect = False
else:
    if_number_incorrect = False

# Print the result:
if if_number_incorrect == True:
    print(f"{price:.2f}")
else:
    print("error")


$separator
