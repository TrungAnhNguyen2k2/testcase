N = int(input())
while N>0:
    s = input()+" "
    s1=""
    count =1
    for i in range(1,len(s)):
        if s[i]==s[i-1]: count+=1
        else:
            s1+= (str(count)+s[i-1])
            count =1
    print(s1)
    N-=1