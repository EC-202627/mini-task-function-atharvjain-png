def finecalc(title, days, rate, limit=150.0):
    total = days * rate
    if total > limit:
        total = limit
    return total

title = input()
days = int(input())
rate = int(input())

amount = finecalc(title, days, rate)

print("Book:", title)
print("Days overdue:", days)
print("Fine: Rs.", float(amount))