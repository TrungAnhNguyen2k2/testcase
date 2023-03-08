from itertools import combinations


n,k = map(int,input().split())
a = set(input().split())
a = sorted(a)
com =combinations(a,k)
# com = sorted(com)
for i in com:
    print(*i)