import math

# Reading input data
num_tournaments = int(input())
starting_points = int(input())

total_points = starting_points
won_tournaments = 0

# Calculating points for each tournament
for _ in range(num_tournaments):
    result = input()
    if result == "W":
        total_points += 2000
        won_tournaments += 1
    elif result == "F":
        total_points += 1200
    elif result == "SF":
        total_points += 720

sum_only_tournaments = total_points - starting_points

# Calculating average points and percentage of won tournaments
average_points = math.floor(sum_only_tournaments / num_tournaments)
percentage_won = (won_tournaments / num_tournaments) * 100

# Printing the result
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percentage_won:.2f}%")