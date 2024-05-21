# User input
n = int(input())

total_sales = 0
total_rating = 0

# Looping for each computer model
for _ in range(n):
    # Reading the input for each computer model
    model_data = int(input())

    # Extracting the last digit (rating)
    rating = model_data % 10

    # Extracting the remaining digits (sales)
    sales = model_data // 10

    # Calculating the percentage of sales based on the rating
    if rating == 2:
        sales_percentage = 0
    elif rating == 3:
        sales_percentage = 0.5
    elif rating == 4:
        sales_percentage = 0.7
    elif rating == 5:
        sales_percentage = 0.85
    elif rating == 6:
        sales_percentage = 1

    # Calculating actual sales for the current model
    actual_sales = sales * sales_percentage

    # Adding the actual sales and rating to the total
    total_sales += actual_sales
    total_rating += rating

average_rating = total_rating / n

# Print the results:
print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")