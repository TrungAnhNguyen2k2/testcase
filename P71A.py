n = int(input())
while n>0:
    st = input()
    s = " "
    if len(st)>10:
        s = st[0] + str(len(st)-2) + st[len(st)-1]
        print (s)
    else: 
        print(st)
    n = n-1