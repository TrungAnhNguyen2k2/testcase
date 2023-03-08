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
n,m = map(int,input().split())
a = list()
c = list()
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
for i in range(n):
    for j in range(m):
        if kiemtranguyento(a[i][j])==1:
            c.append(a[i][j])
# print(c)
if len(c)==0: print("NOT FOUND")
else:
    a1 = max(c)
    print(a1)
    for i in range(n):
        for j in range(m):
            if a[i][j]== a1:
                print("Vi tri ","[",i,"]","[",j,"]", sep="")
