def calculate_fine(book_title, days_overdue, daily_rate, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


line = input()
parts = line.split()

days_overdue = int(parts[-2])
daily_rate = int(parts[-1])

book_title = " ".join(parts[:-2])

fine = calculate_fine(book_title, days_overdue, daily_rate)

print("Book:", book_title, "Days overdue:", days_overdue, "Fine: Rs.", float(fine))