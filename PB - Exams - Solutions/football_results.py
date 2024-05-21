result1 = input()
result2 = input()
result3 = input()

wins = 0
losses = 0
draws = 0

if int(result1[0]) > int(result1[2]):
    wins += 1
elif int(result1[0]) < int(result1[2]):
    losses += 1
else:
    draws += 1

if int(result2[0]) > int(result2[2]):
    wins += 1
elif int(result2[0]) < int(result2[2]):
    losses += 1
else:
    draws += 1

if int(result3[0]) > int(result3[2]):
    wins += 1
elif int(result3[0]) < int(result3[2]):
    losses += 1
else:
    draws += 1

# Отпечатване на резултата
print(f'Team won {wins} games.')
print(f'Team lost {losses} games.')
print(f'Drawn games: {draws}')