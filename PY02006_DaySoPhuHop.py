t = int(input())
for i in range (t):
    check =1
    n = int (input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range (n):
        if a[i]> b[i]:
            check =0
            print("NO")
            break
    if check ==1: print("YES")