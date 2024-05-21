budget = float(input())
season = input()
place = ""
type = ""
money_spend = 0


if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        type = "Camp"
        money_spend = budget * 0.30
    elif season == "winter":
        type = "Hotel"
        money_spend = budget * 0.70
elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        money_spend = budget * 0.40
        type = "Camp"
    if season == "winter":
        type = "Hotel"
        money_spend = budget * 0.80
elif budget > 1000:
    type = "Hotel"
    place = "Europe"
    money_spend = budget * 0.90

print(F"Somewhere in {place}")
print(f"{type} - {money_spend:.2f}")