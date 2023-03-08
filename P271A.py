year = int(input())
check = True
while check == True:
    year = year +1
    year1 = year
    a=[]
    while year1>0:
        a.append(year1%10)
        year1 = int(year1/10)
    if a[0] != a[1] and a[0] != a[2] and a[0] != a[3] and a[1] != a[2]  and a[1] != a[3] and a[2] != a[3]: break
print(year)
