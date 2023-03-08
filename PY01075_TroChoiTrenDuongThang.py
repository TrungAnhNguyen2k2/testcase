t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b ={}
    for i in range(n):
        b[a[i]]=c[i]
    b = sorted(b.items())
    d =[]
    # print(b[0][0])
    check =1
    for i in range (n-1):
        if b[i+1][0]-b[i][0]==1:
            d.append(b[i+1][1]+b[i][1])
            check =1
            
        else:
            check =0
    if check ==0:print(-1)
    else: print(min(d))
    