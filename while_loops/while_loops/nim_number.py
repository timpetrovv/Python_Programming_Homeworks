min_number = None

while True:
    input_value = input()

    if input_value == "Stop":
        break

    try:
        current_number = int(input_value)

        if min_number is None or current_number < min_number:
            min_number = current_number

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if min_number is not None:
    print(min_number)
else:
    print("No numbers were entered.")