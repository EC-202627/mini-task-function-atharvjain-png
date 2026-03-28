def finecalc(title, days, rate=5.0, limit=150.0):
    total = days * rate
    if total > limit:
        total = limit
    return total

title = input()
days = int(input())

amount = finecalc(title, days)

print("Book:", title)
print("Days overdue:", days)
print("Fine: Rs.", float(amount))

if amount == 150.0:
    print("You have accumulated the maximum fine of INR:", float(amount))