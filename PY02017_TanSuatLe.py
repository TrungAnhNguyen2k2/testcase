from collections import Counter
t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    a = Counter(a)
    for i in a:
        if a[i]%2:
            print(i)
            break