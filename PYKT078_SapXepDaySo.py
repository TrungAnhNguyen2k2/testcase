n = int(input())
for i in range(n):
    x, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list()
    c = list()
    for i in range(x):
        if a[i]==max(a):
            a.insert(i,m)
            break
    for i in range(len(a)):
        if a[i]<0:
            b.append(a[i])
        else: c.append(a[i])
    print(*b,*c, sep=" ")
