t = int(input())
for i in range(t):
    max1=""
    max2=""
    min1=""
    min2=""
    p,q = list(input().split())
    if int(p)>int(q):
        p,q=q,p
    s = input()
    try:
        x1,x2 = s.split()
    except :
        x1 =s
        x2=input() 
    max1= x1.replace(p,q)
    min1= max1.replace(q,p)
    max2= x2.replace(p,q)
    min2= max2.replace(q,p)
    # print(int(min1))
    # print(int(min2), int(max2))
    max= int(max1)+int(max2)
    min = int(min1)+int(min2)
    print(min,max)