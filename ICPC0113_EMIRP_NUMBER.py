def sangnguyento(n):
    a = [True for i in range(n+1)]
    p =2
    while(p*p<=n):
        if(a[p]==True):
            for i in range(p**2,n+1,p):
                a[i]=False
        p+=1
    a[0]=False
    a[1]=False
    b = list()
    for i in range(len(a)):
        if a[i]==True: b.append(i)
    return b
t = int(input())
for i in range(t):
    n = int(input())
    a = sangnguyento(n)
    b = list()
    for i in a:
        if (str(i)!=str(i)[::-1] and int(str(i)[::-1]) in a ) and i not in b:
            b.append(i)
            b.append(int(str(i)[::-1]))
    print(*b)