n = int(input())
while n>0:
    s = input()
    s1 =""
    for i in range(len(s)-1):
        if i %2==0:
            s1 += (s[i]*(int(s[i+1])))
    print(s1)
    n-=1