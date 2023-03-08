from decimal import ROUND_HALF_UP, Decimal

n = int(input())
while n>0:
    a= int(input())
    p = 10
    i = 1
    while a>p:
        r = '1E'+str(i)
        a = int(Decimal(str(a)).quantize(Decimal(r), rounding=ROUND_HALF_UP))
        i += 1
        p *= 10
    print(a)
    n = n-1
# 7
# 15
# 14
# 5
# 99
# 12345678
# 44444445
# 1445