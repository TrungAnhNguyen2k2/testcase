def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
n = int(input())
while n>0:
    s = input()
    sum =0
    for i in s:
        sum+=int(i)
    s1 = str(sum)
    
    # print(s1)
    if str(sum) == reverse(s1) and sum>10 : print("YES")
    else: print("NO")
    n-=1