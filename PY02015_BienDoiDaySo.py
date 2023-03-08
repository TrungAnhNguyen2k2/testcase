a = []
while a !=[0,0,0,0]:
    a = list(map(int, input().split()))
    if a ==[0,0,0,0]: break
    dem =0
    while a[0] !=a[1] or a[1]!=a[2] or a[2]!=a[3] or a[3]!=a[0]:
        dem +=1
        tmp = a[0]
        a[0]=abs(a[0]-a[1])
        a[1]= abs(a[1]-a[2])
        a[2] = abs(a[2]-a[3])
        a[3]= abs(a[3]-tmp)
    print(dem)