n = int(input())
x= 0
for i in range(n):
    str = input()
    s = str.strip('X')
    if s == "++":
        x+=1
    elif s =="--":
        x-=1
print(x)