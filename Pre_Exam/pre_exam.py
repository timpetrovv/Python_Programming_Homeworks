# Reading player names
player1_name = input()
player2_name = input()

# Initializing points for each player
player1_points = 0
player2_points = 0

# Game loop
while True:
    card_player1 = input()
    card_player2 = input()

    if card_player1 == "End of game" or card_player2 == "End of game":
        break

    card_player1 = int(card_player1)
    card_player2 = int(card_player2)

    if card_player1 > card_player2:
        player1_points += card_player1 - card_player2
    elif card_player2 > card_player1:
        player2_points += card_player2 - card_player1
    else:
        # Number wars
        print("Number wars!")
        extra_card_player1 = int(input())
        extra_card_player2 = int(input())

        if extra_card_player1 > extra_card_player2:
            #player1_points += extra_card_player1 - extra_card_player2
            winner_name = player1_name
            print(f"{winner_name} is winner with {abs(player1_points)} points")
            break
        else:
            #player2_points += extra_card_player2 - extra_card_player1
            winner_name = player2_name
            print(f"{winner_name} is winner with {abs(player2_points)} points")
            break

# Print the final scores only if the loop ends without "Number wars!"
if card_player1 == "End of game" or card_player2 == "End of game":
    print(f"{player1_name} has {player1_points} points")
    print(f"{player2_name} has {player2_points} points")