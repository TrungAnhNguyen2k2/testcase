n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c ={0}
for i in range(1, len(a)):
     c.add(a[i])
for i in range(1, len(b)):
     c.add(b[i])
c.remove(0)
# print(*c)
if(n ==len(c)): print("I become the guy.")
else: print("Oh, my keyboard!")