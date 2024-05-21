

# Input
n = int(input())
first_pair = 0
second_pair = 0

# Logic
for _ in range(n):   #2 times executed
    first_cycle_number = int(input()) #90
    first_pair += first_cycle_number #10

for num in range(n):
    second_cycle_number = int(input())
    second_pair += second_cycle_number

#print(first_pair)
#print(second_pair)

if first_pair == second_pair:
    print(f"Yes, sum = {first_pair} ")
else:
    first_pair -= second_pair
    print(f"No, diff = {abs(first_pair)}")





