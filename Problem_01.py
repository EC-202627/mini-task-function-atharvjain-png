def calculate_fine(book_title, days_overdue, daily_rate=5.00, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine

line = input()

# Splitting: last word = days, rest = book title
parts = line.rsplit(" ", 1)
book_title = parts[0]
days_overdue = int(parts[1])

fine = calculate_fine(book_title, days_overdue)

print(f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}")

