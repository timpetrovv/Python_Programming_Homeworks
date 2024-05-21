book_pages = int(input())
number_pages = int(input())
number_days = int(input())

Total_pages_per_day = book_pages / number_pages
Days_to_complete = int(Total_pages_per_day / number_days)

print(Days_to_complete)