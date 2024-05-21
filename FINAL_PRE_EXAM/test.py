K = int(input())
L = int(input())
M = int(input())
N = int(input())

valid_changes_count = 0

for number1_first_digit in range(K, 9, 2):
    print(number1_first_digit)

for number1_second_digit in reversed(range(9, L + 1, 2)):
    print(number1_second_digit)

#        for number2_first_digit in range(M, 9, 2):
 #           print(number2_first_digit_digit)
#            for number2_second_digit in range(9, N + 1, 2):
  #              print(number3_first_digit_digit)
#



#                if number1_first_digit % 2 == 0 and number1_second_digit % 2 == 1 and number2_first_digit % 2 == 0 and number2_second_digit % 2 == 1:
#                    valid_changes_count += 1
#                    if valid_changes_count == 1:
#                        print(f"{number1_first_digit}{number1_second_digit} - {number2_first_digit}{number2_second_digit}")
#                    else:
#                        print(f"{number1_first_digit}{number1_second_digit} - {number2_first_digit}{number2_second_digit}")