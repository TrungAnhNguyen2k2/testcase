a =[2,3,4,5,5,4,2,-1]
a.sort()
b =[a[0]]
for i in a:
    if i!=b[-1]:
        b.append(i)
print(b)