K = int(input())
L = int(input())
M = int(input())
N = int(input())

# Count the number of valid player changes:
valid_changes = 0

for first_digit_first_number in range(K, 9):
    # print(first_digit_first_number)
    for second_digit_first_number in range(9, L - 1,- 1):
    #    print(second_digit_first_number)
        for first_digit_second_number in range(M, 9):
    #        print(second_digit_first_number)
            for second_digit_second_number in range(9, N - 1, -1):
    #            print(second_digit_first_number)
                if first_digit_first_number % 2 == 0 and second_digit_first_number % 2 == 1 and first_digit_second_number % 2 == 0 and second_digit_second_number % 2 == 1:
                    if first_digit_first_number != first_digit_second_number or second_digit_first_number != second_digit_second_number:
                        print(f"{first_digit_first_number}{second_digit_first_number} - {first_digit_second_number}{second_digit_second_number}")
                        valid_changes += 1
                        if valid_changes == 6:
                            break
                    else:
                        print("Cannot change the same player.")

            if valid_changes == 6:
                break
        if valid_changes == 6:
            break
    if valid_changes == 6:
        break