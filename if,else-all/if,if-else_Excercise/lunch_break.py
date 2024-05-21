from math import ceil

name_series = input()
time_episode = int(input())
time_break = int(input())

launch_1 = time_break * 0.125
launch_2 = time_break * 0.25
total_launch = launch_2 + launch_1

total = time_break - launch_1 - launch_2

if total >= time_episode:
    left = total - time_episode
    left = ceil(left)
    print(f"You have enough time to watch {name_series} and left with {left} minutes free time.")
elif total < time_episode:
    needed = time_episode - total
    needed = ceil(needed)
    print(f"You don't have enough time to watch {name_series}, you need {needed} more minutes.")