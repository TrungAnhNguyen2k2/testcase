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
n = int(input())
while n>0:
    s = input()
    sum =0
    for i in s:
        sum+=int(i)
    if kiemtranguyento(sum)==1: print("YES")
    else: print("NO")
    n-=1