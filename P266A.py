n = int(input())
s = input()
r=0
b=0
g =0
for i in range(1,n):
    if s[i]==s[i-1]:
        if s[i]=="R": r+=1
        elif s[i]=="B": b+=1
        elif s[i]=="G": g+=1
# print(r)
# print(g)
# print(b)
print(r+b+g)
