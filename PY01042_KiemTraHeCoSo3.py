n = int(input())
for i in range(n):
    s = input()
    check =1
    for i in s:
        if i !="0" and i!="1" and i !="2":
            check =0
            break
    if check ==1: print("YES")
    else: print("NO")