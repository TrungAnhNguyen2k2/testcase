t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = a[k:]+a[0:k]
    print(*b)