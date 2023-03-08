N = int(input())
while N>0:
    s = input()
    check =1
    for i in range (len(s)-1):
        if s[i]>s[i+1]: 
            check =0
            break
    if check ==1: print("YES") 
    else: print("NO")  
    N-=1