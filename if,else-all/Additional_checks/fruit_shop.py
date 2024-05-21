# User input
fruit = input()
day_week = input()
quantity = float(input())
price = 0
is_input_valid = True
# Logic

if day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday" or day_week == "Thursday" or day_week == "Friday":
    if fruit == "banana":
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity * 1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.70
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == "grapes":
        price = quantity * 3.85
    else:
        is_input_valid = False
elif day_week == "Saturday" or day_week == "Sunday":
    if fruit == "banana":
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3.00
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.20
    else:
        is_input_valid = False
else:
    is_input_valid = False

if is_input_valid == False:
    print("error")
else:
    print(f"{price:.2f}")
