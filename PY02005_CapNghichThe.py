n = int(input())
dem =0 
a = list(map(int, input().split()))
for i in range (n-1):
    for j in range (i,n):
        if a[i]>a[j]: dem +=1
print(dem)