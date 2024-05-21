number = int(input())
input_numbers = 0
total_numbers = 0

while True:
    input_numbers = int(input())
    total_numbers += input_numbers
    if total_numbers >= number:
        break;

print(total_numbers)
