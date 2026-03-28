def calculate_fine(book_title, days_overdue, daily_rate, max_fine):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


book_title = input()
days_overdue = int(input())
daily_rate = int(input())
max_fine = int(input())

fine = calculate_fine(book_title, days_overdue, daily_rate, max_fine)

print("Book:", book_title)
print("Days overdue:", days_overdue)
print("Fine: Rs.", float(fine))
