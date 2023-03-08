n = int(input())
a= []
groups = 1
while n>0:
    a.append(input())
    n=n-1
for i in range(len(a)-1):
    if  a[i]!=a[i+1]: 
        groups+=1
print(groups)
