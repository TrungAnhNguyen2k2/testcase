n = int(input())
a =list()
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
b = list()
c = list()
for i in range(n-1):
    for j in range(0,n-i-1):
        b.append(a[i][j])
# print(b)
for i in range(1,n):
    for j in range(n-i,n):
        c.append(a[i][j])
# print(c)
b = sum(i for i in b)
c = sum(i for i in c)
print("YES") if abs(b-c)<=k else print("NO")
print(abs(c-b))