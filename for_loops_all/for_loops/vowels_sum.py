word = input()
total_numbers = 0

for i in range(0,len(word)):
    if word[i] == "a":
        total_numbers += 1
    if word[i] == "e":
        total_numbers += 2
    if word[i] == "i":
        total_numbers +=3
    if word[i] == "o":
        total_numbers +=4
    if word[i] == "u":
        total_numbers += 5
print(total_numbers)