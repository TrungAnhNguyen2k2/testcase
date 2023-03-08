import collections

t = int(input())
for i in range (t):
    n = int(input())
    a = []
    for j in range(n):
        a.append(int(input()))
    # print(a)
    a.sort()
    c = collections.Counter(a)
    print(c.most_common()[0][0])