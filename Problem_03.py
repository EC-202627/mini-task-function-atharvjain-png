def calculatefine(booktitle, daysoverdue, dailyrate=5.0, maxfine=150.0):
    fine = daysoverdue * dailyrate
    if fine > maxfine:
        fine = maxfine
    return fine

booktitle = input()
daysoverdue = int(input())

fine = calculatefine(booktitle, daysoverdue)

print("Book:", booktitle)
print("Days overdue:", daysoverdue)
print("Fine: Rs.", float(fine))

if fine == 150.0:
    print("You have accumulated the maximum fine of INR:", float(fine))