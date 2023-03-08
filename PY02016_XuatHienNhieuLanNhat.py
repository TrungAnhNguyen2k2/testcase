import collections


t = int(input())
for i in range (t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = collections.Counter(a)
    b=[int]
    if max(c.values())<=n/2:
        print("NO")
    else:
        print(c.most_common()[0][0])