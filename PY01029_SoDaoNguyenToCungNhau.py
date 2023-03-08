from math import gcd


n = int(input())
for i in range (n):
    s = input()
    s1 = s[::-1]
    if gcd(int(s),int(s1))==1:print("YES")
    else: print("NO")