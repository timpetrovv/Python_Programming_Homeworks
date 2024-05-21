n = int(input())
salary = int(input())
money_taken = 0

for _ in range(n):
    tab = input()
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50
    if salary == 0:
        break

if salary == 0:
    print(f"You have lost your salary.")
else:
    print(salary)