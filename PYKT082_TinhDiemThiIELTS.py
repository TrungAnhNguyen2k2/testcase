from math import ceil
t = int(input())
def doidiem(a):
    if a >= 3 and a <=4:
        return 2.5
    elif a>=5 and a <=6:
        return 3.0
    elif a>=7 and a <=9:
        return 3.5
    elif a>=10 and a <=12:
        return 4.0
    elif a>=13 and a <=15:    
        return 4.5
    elif a>=16 and a <=19:
        return 5.0
    elif a>=20 and a <=22:
        return 5.5
    elif a>=23 and a <=26:
        return 6
    elif a>=27 and a <=29:
        return 6.5
    elif a>=30 and a <=32:
        return 7
    elif a>=33 and a <=34:
        return 7.5
    elif a>=35 and a <=36:
        return 8
    elif a>=37 and a <=38:
        return 8.5
    else: return 9
    
for i in range(t):
    a,b,c,d = map(float,input().split())
    x = doidiem(a)+doidiem(b)+c+d
    x/=4
    if(x-int(x)<0.25):    
        print(int(x)+0.0)
    elif x - int(x)>= 0.75:    
        print(int(x)+1.0)
    else: 
        print(int(x)+0.5)
