n = int(input())
for i in range(n):
    s1 = input()
    s2 = s1[::-1]
    # print(len(s1), len(s2))
    check =1
    for i in range(1,len(s2)):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])):
            check =0
    if check == 1: print("YES")
    else: print("NO")