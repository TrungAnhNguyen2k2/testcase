def dem(s1,s2):
    dem =0
    for i in s2:
        if i== str(s1):
            dem +=1
    return dem
N = int(input())
for i in range(N):
    l,r = map(int, input().split())
    s =""
    for j in range(l,r+1):
        s+=str(j)
    for k in range(0,10):
        print(dem(k,s),end=" ")
    print()