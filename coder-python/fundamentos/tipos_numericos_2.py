from decimal import Decimal, getcontext

print(Decimal(1) / Decimal(7))
getcontext().prec = 4
print(Decimal(1) / Decimal(7))