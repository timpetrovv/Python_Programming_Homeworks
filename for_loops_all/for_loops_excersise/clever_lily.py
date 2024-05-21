years = int(input())
washing_mashing_prise = float(input())
price_one_toy = int(input())
brother_stealing = 0

money_received = 0
toys_count = 0

for n in range(1,years+1):
    if n % 2 == 0:
        money_received += (n/2) * 10
        brother_stealing += 1
    else:
        n % 2 != 0
        toys_count += 1
    print(n)

toys_count *= price_one_toy
money_received += toys_count
money_received -= brother_stealing
if money_received >= washing_mashing_prise:
    print(f"Yes! {money_received-washing_mashing_prise:.2f}")
else:
    print(f"No! {washing_mashing_prise-money_received:.2f}")

