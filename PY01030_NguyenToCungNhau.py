import math


n,k = list(map(int, input().split()))
dem =0
for i in range(pow(10,k-1),pow(10,k)):
    if math.gcd(i,n)==1:
        print(i, end=" ")
        dem +=1
        if dem ==10: 
            print()
            dem =0