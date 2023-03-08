t = int(input())
for i in range(t):
    n = int (input())
    a = list(input().split())
    a = sorted(a,key= lambda s: (sum(int(i)for i in s),int(s)))
    print(*a)

