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
    check =0
    if kiemtranguyento(len(s))==1:
        count =0
        for i in s: 
            if kiemtranguyento((int(i)))==1: count+=1
            else: count-=1
        if count>0: check=1
    if check ==1: print("YES")
    else: print("NO")