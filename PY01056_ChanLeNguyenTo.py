def sum(s):
    sum =0
    for i in s:
        sum+= int(i)
    return sum 
def kiemtranguyento(k):
    check =1
    if (k <2):
        check = 0
        return check

    for p in range(2, k):
        if k % p == 0:
            check = 0
            break
    return check
def checkchanle(i):
    check =1
    if i %2!=0: check =0
    return check 
n = int(input())
for i in range(n):
    s = input()
    check =1
    # print(sum(s))
    if kiemtranguyento(sum(s))==1:
        for i in range(len(s)):
            if checkchanle(i)!= checkchanle(int(s[i])): 
                check =0
                break
        if check ==1:print("YES")
        else: print("NO")
    else: print("NO")