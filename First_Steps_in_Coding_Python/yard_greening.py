# User input squared meters
squared_meters = float(input())

# Calcualte Price without discount. - Price for Squared meter 7.61
nodiscount_price = squared_meters * 7.61

# Calculate Discount Price. With 18% off the the Total price.
discount_price= 0.18 * nodiscount_price

# Calcualte the Final price.
final_price = nodiscount_price - discount_price

# Output of the console in the following Format:
# "The final price is: {крайна цена на услугата} lv."
# "The discount is: {отстъпка} lv.

print(f"The Final price is: {final_price} lv.")
print(f"The discount is: {discount_price} lv.")

