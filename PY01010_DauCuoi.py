n = int(input())
while n>0:
    s = input()
    s1 = s[0:2]
    s2 = s[-2:]
    if s1 == s2: print("YES")
    else: print("NO")
    n-=1
