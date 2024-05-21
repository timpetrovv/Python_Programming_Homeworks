max_number = None

while True:
    input_value = input()

    if input_value == "Stop":
        break

    try:
        current_number = int(input_value)

        if max_number is None or current_number > max_number:
            max_number = current_number

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if max_number is not None:
    print(max_number)
else:
    print("No numbers were entered.")