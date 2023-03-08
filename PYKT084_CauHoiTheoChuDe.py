n = int(input())
a = list()
s = ''
for i in range(n) :
    a.append(input())
a.append("")
dem =0
for i in range (len(a)):
    if a[i] !="":
        dem +=1
    else:
        print(a[i-dem],": ",dem-1, sep="")
        dem =0
