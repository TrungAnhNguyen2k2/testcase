N = int(input())

for i in range(N):
    n = input()
    
    sum =0
    for i in range(1000):
        if int(n)%7==0:
            break
        n1 = n[::-1]
        sum = (int(n) + int(n1))
        n = str(sum)
        if sum %7 ==0:
            break
    if int(n) %7 ==0: print(int(n)) 
    elif sum%7==0: print(sum)
    else: print(-1)