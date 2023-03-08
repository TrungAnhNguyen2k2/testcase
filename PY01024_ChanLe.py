def sum(s):
    sum=0
    for i in s:
        sum+=int(i)
    return sum
n = int(input())
for i in range(n):
    s = input()
    check =1
    if sum(s)%10==0:
        for i in range(len(s)-1):
            if abs(int(s[i]) - int(s[i+1])) !=2:
                check =0
    else : check =0
    if check ==1: print("YES")
    else: print("NO")
