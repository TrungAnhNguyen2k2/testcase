from itertools import combinations, permutations


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    dem =0
    for i in range(len(a)-2):
        l = i+1
        r = len(a)-1
        while l<r:
            if a[i]+a[l]+a[r]==0:
                dem +=1
                l+=1
            elif a[i]+a[l]+a[r]>0:
                r -=1
            else:
                l+=1
    print(dem)
    # perm = combinations(a,3)
    # dem =0
    # for i in perm:
    #     sum =0
    #     for j in i:
    #         sum +=j
    #     if sum ==0:
    #         dem +=1
    #     print(dem)
