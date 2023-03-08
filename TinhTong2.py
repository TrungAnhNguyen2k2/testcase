t = int(input())
for i in range(t):
    sum=0
    n,k = map(int,input().split())
    for i in range(n+1):
        sum += (i**k)
    print(sum)