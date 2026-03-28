def finecalc(title, days, rate, limit):
    total = days * rate
    if total > limit:
        total = limit
    return total

title = input()
days = int(input())
rate = int(input())
limit = int(input())

amount = finecalc(title, days, rate, limit)

print("Book:", title)
print("Days overdue:", days)
print("Fine: Rs.", float(amount))
