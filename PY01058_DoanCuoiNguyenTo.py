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
for n in range(N):
    s = input()
    s1 = int(s[-4:])
    if kiemtranguyento(s1)==1: print("YES")
    else: print("NO")