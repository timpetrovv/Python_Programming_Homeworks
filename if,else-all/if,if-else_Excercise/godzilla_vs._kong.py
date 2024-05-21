budget_film = float(input())
count_statists = int(input())
cloth_statists = float(input())

decor = budget_film * 0.10

price_statists = count_statists * cloth_statists

if count_statists > 150:
    price_statists *= 0.90

total_spending = decor + price_statists

if total_spending > budget_film:
    print(f"Not enough money!")
    needed = total_spending - budget_film
    print(f"Wingard needs {needed:.02f} leva more.")
elif total_spending <= budget_film:
    print(f"Action!")
    extra = budget_film - total_spending
    print(f"Wingard starts filming with {extra:.02f} leva left.")