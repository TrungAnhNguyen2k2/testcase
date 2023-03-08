# a,k,n = list(map(int, input().split()))
# b =[-1]
# c = int((n-a)/k)
# for i in range (a,c):
#     b.append(i*k-a)
# if len(b)!=1: b.remove(-1)
# print(*b)
from math import ceil
a,k,n = map(int,input().split())
left = a/k
if left == int(left): left = int(left)+1
else: left = ceil(left)
left*= k 
a = [(i - a) for i in range(left,n+1,k)]
print(-1) if len(a)==0 else print(*a)
