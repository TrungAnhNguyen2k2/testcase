def mul(s):
    mul =1
    for i in s:
        mul*=int(i)
    return mul

t = int(input())

for i in range(t):
    n = int (input())
    a = list(input().split())
    a = sorted(a,key= lambda s: (mul(s),int(s)))
    print(*a)
