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
    check =1
    for i in range(len(s)-1):
        if kiemtranguyento(i) != kiemtranguyento(int(s[i])):
            check =0
    if check ==1: print("YES")
    else: print("NO")