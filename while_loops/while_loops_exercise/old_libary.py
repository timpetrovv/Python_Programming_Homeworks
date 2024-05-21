searched_book = input()
books_counted = 0
book_is_found = False

while True:
    current_book = input()
    if current_book == searched_book:
        book_is_found = True
        break
    elif current_book == "No More Books":
        break
    books_counted += 1

if book_is_found:
    print(f"You checked {books_counted} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books_counted} books.")
