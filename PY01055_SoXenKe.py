n = int(input())
for i in range(n):
    s = input()
    check = 1
    if len(s)%2!=0:
        if s[0]!=s[1]:
            for i in range(0,len(s)-1,2) :
                if s[i]!=s[i+2]: check=0
        else: check =0
    else: check =0
    if check ==1: print("YES")
    else: print("NO")
