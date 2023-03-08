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
for i in range(n):
    s = input()
    s1 =s[0:3]
    s2 = s[-3::]
    if kiemtranguyento(int(s1))==1 and kiemtranguyento(int(s2))==1: print("YES")
    else: print("NO")