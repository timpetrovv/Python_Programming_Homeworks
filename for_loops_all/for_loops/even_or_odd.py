n = int(input())
odds_sum = 0
even_sum = 0

# Logic
for i in range(n):
    first_cycle_number = int(input())
    if i % 2 == 0:
        even_sum += first_cycle_number
    elif i % 2 != 0:
        odds_sum += first_cycle_number

if even_sum == odds_sum:
    print(f"Yes")
    print(f"Sum = {abs(even_sum)}")
else:
    odds_sum -= even_sum
    print(f"No")
    print(f"Diff = {abs(odds_sum)}")

#print()

#for num in range(n):
#    second_cycle_number = int(input())
#   second_pair += second_cycle_number

#print(first_pair)
#print(second_pair)

#if first_pair == second_pair:
#    print(f"Yes, sum = {first_pair} ")
#else:
#    first_pair -= second_pair
#    print(f"No, diff = {abs(first_pair)}")





