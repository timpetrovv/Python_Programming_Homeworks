the_best_player = ""
max_goals = 0
hat_trick = False

while True:
    player = input()

    # End the loop of the player name is set to "END"
    if player == "END":
        break

    goals = int(input())

    if goals >= 3:
        hat_trick = True

    if goals > max_goals:
        the_best_player = player
        max_goals = goals

    # End the loop if goals are 10 or more!
    if max_goals >= 10:
        break

print(f"{the_best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")