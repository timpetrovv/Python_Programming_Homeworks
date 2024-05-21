n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0,n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number >= 200 and number <= 399:
        p2 += 1
    elif number >= 400 and number <= 599:
        p3 += 1
    elif number >= 600 and number <= 799:
        p4 += 1
    elif number >= 800:
        p5 += 1

first_number = p1/n * 100
print(f"{first_number:.2f}%")
second_number = p2/n * 100
print(f"{second_number:.2f}%")
third_number = p3/n * 100
print(f"{third_number:.2f}%")
forth_number = p4/n * 100
print(f"{forth_number:.2f}%")
fifth_number = p5/n * 100
print(f"{fifth_number:.2f}%")


#print(p1)
#print(p2)
#print(p3)
#print(p4)
#print(p5)


#        numbers = int(input())
#       if numbers < 200:
 #           p1 += 1
 #       elif numbers >= 200 or numbers < 399:
 #           p2 += 1
 #       elif numbers >= 400 or numbers < 599:
 #           p3 += 1
 #       elif numbers >= 600 or numbers < 799:
 #           p4 += 1
 #       elif numbers >= 800:
 #           p5 += 1



#print(number)