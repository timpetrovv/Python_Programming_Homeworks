# User input the deposit sum.
deposit_sum = float(input())

# User Input the Deposit of months.
deposit_months = int(input())

# User Input the Deposit of interest percent.
interest_percent = float(input())

# Calculate the interest price.
interest_price = deposit_sum * interest_percent / 100

# Calculate the price for 1 month.
monthly_interest = interest_price / 12

# Calculate Total price
total_price = print(deposit_sum + deposit_months * monthly_interest)

print(total_price)