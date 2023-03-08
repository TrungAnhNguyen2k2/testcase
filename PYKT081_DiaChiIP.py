n = int(input())
for i in range(n):
    x = input()
    try:
        a = list(map(int,x.split(".")))
        check =1
        for i in a:
            if i <0 or i >255:
                check =0
                break
        if len(a)!=4: check =0
        if  check==1: print("YES")
        else: print("NO")
    except:
        print("NO")
