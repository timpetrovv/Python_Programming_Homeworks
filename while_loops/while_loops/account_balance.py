total_balance = 0

while True:
    input_value = input()

    if input_value == "NoMoreMoney":
        break

    try:
        amount = float(input_value)
        if amount >= 0:
            total_balance += amount
            print(f"Increase: {amount:.2f}")
        else:
            print("Invalid operation!")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

print(f"Total: {total_balance:.2f}")