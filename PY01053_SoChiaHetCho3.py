n = int(input())
while n>0:
    s = input()
    sum =0
    for i in s:
        sum +=int(i)
    if sum %3==0: print("YES")
    else: print("NO")
    n-=1