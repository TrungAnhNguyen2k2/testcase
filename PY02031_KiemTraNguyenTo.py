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
n, m = list(map(int,input().split()))
b = list()
for i in range(n):
    a = [kiemtranguyento(int(i)) for i in input().split()]
    # print(*a)
    b.append(a)
for i in range(n):
    print(*b[i])

# print(*b)
