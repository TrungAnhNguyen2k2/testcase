t = int(input())
for i in range(t):
    n = int(input())
    f= [0]*(n+1)
    x,y,z = [int(x)for x in input().split()]
    f[1]=x
    for i in range(2,n+1):
        if i %2==0:
            f[i] = min(f[i-1]+x,f[i//2]+z)
        else:
            f[i] = min(f[i-1]+x,f[i//2+1]+z+y)
    print(f[n])