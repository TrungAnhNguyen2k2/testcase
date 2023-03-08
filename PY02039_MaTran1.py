n = int(input())
a =list()
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
b = list()
c = list()
for i in range(n):
    for j in range(i+1,n):
        b.append(a[i][j])
for i in range(1,n):
    for j in range(i):
        c.append(a[i][j])
b = sum(i for i in b)
c = sum(i for i in c)
print("YES") if abs(b-c)<=k else print("NO")
print(abs(c-b))