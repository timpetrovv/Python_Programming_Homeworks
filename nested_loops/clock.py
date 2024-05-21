for h in range(24):
    for m in range (60):
        print(f"{h}:{m}")


for x in range(1, 11):
    for y in range(1, 11):
        result = x * y
        print(f'{x} * {y} = {result}')

number = int(input())
combination_counter = 0

for x1 in range (number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            if x1 + x2 + x3 == number:
                combination_counter += 1

print(combination_counter)


start_interval = int(input())
final_interval = int(input())
magic_number = int(input())

combination_counter = 0
condition = False

for first_number in range(start_interval, final_interval + 1):
    for second_number in range(start_interval, final_interval + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            print(f'Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})')
            condition = True
            break

    if condition:
            break

else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")




floors = int(input())
rooms_per_floor = int(input())

for floor in reversed(range(1, floors + 1)):
    room_type = "A" if floor % 2 else '0'

    if floors == floors:
        room_type = "L"

    for room in range(rooms_per_floor):
        room_name = f'{room_type}{floor}{room}'
        print(room_name, end=' ')

    print()