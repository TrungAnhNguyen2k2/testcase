n = int(input())
for i in range (n):
    s = input()
    check =1
    for i in range(len(s)-1):
        if s[i]== s[i+1]: check =0
    for i in range(len(s)-2):
        if s[i]!= s[i+2]: check =0
    if check ==1:print("YES")
    else: print("NO")
