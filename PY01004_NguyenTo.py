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
    n = int(input())
    k =0
    for i in range(1,n):
        if math.gcd(i,n)==1: k+=1
    # print(k)
    if kiemtranguyento(k)==1: print("YES")
    else: print ("NO")
    N=N-1