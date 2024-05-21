hour_input = int(input())
day_week = input()

if hour_input >= 10 and hour_input <= 18 and day_week != "Sunday":
    print("open")
else:
    print("closed")