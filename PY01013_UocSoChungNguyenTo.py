import math
def kiemtranguyento(k):
    check =1
    if (k <2):
        check = 0
        return check
    for p in range(2, k):
        if k % p == 0:
            check = 0
            break
    return check
N = int(input())
while N>0:
    a, b = list(map(int,input().split()))
    c = math.gcd(a,b)
    sum =0
    while c>0:
        sum+= c%10
        c =int(c/10)
    if kiemtranguyento(sum)==1: print("YES")
    else: print("NO")
    N-=1