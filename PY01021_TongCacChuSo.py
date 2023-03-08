n = int(input())
for i in range(n):
    s = input()
    b = list()
    c = list()
    for i in s:
        if i.isalpha()==True:
            b.append(i)
        elif i.isnumeric()==True:
            c.append(int(i))
    tong = sum(c)
    b = sorted(b)
    s=""
    for i in b:
        s+=i
    s+= str(tong)
    print(s)