n = int(input())
a = list()
b = list()
c = list()
while len(a)<n:
    a.extend(list(map(int,input().split())))
for i in range(len(a)):
    if a[i]%2==0: b.append(i)
    else: c.append(i)
# print(b,c)
for i in range(len(b)-1):
    for j in range(len(b)-i-1):
        if a[b[j]]>=a[b[j+1]]:
            a[b[j]],a[b[j+1]]=a[b[j+1]],a[b[j]]
for i in range(len(c)-1):
    for j in range(0,len(c)-i-1):
        if a[c[j]]<=a[c[j+1]]:
            a[c[j]],a[c[j+1]]=a[c[j+1]],a[c[j]]
print(*a)