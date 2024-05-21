tshirt_price = float(input())
target_sum = float(input())

# Calculating prices
shorts_price = 0.75 * tshirt_price
socks_price = 0.20 * shorts_price
sneakers_price = 2 * (tshirt_price + shorts_price)

# Calculating total sum
total_price = tshirt_price + shorts_price + socks_price + sneakers_price

# Applying discount
total_sum_after_discount = total_price - (total_price * 0.15)

# Checking if Pepe wins the ball
if total_sum_after_discount >= target_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_after_discount:.2f} lv.")
else:
    needed_money = target_sum - total_sum_after_discount
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money:.2f} lv. more.")