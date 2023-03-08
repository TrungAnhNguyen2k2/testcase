s = int(input())
a = list()
while s>0:
    a.append(s%1000)
    s//=1000
a = a[::-1]
print(a) 