import sys

index = int(input())
max_num = -sys.maxsize
numbers_sum = 0

for _ in range(0, index):
    num = int(input())
    numbers_sum += num
    if num > max_num:
        max_num = num

if max_num == numbers_sum - max_num:
    print("Yes")
    print(f"Sum = {abs(max_num)}")
else:
    print("No")
    diff = numbers_sum - max_num
    max_num -= diff
    print(f"Diff = {abs(max_num)}")

