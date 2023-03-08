import collections
def kiemtranguyento(k):
    check =1
    if (k <2):
        check = 0
        return check
    for p in range(2, k):
        if k % p == 0:
            check = 0
            break
    return check
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
# print(c)
for i in c:
    if kiemtranguyento(i)==1:
        print(i, c[i])
