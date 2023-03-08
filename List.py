def daonguoc(l,r,s):
    b = list()
    for i in range(l,r):
        b.append(s[i])
    for i in range(l,r):
        s[i]=b[r-1-i]
    return s
l = int(input())
r = int(input())
s = [1,2,3,4,5]
print(*daonguoc(l,r+1,s))