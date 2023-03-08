from itertools import combinations
n,k= list(map(int, input().split()))
a = list(set(map(int, input().split())))
a.sort()
perm = combinations(a,k)
for i in list(perm):
    print(*i)
