def fibo(n):
    f0 = 1
    f1 = 1
    fn = 2
 
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return 1
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
n = int(input())

for i in range(n):
    b = []
    l,r = list(map(int,input().split()))
    for i in range(l,r+1):
        # print(fibo(i-1), end=" ")
        b.append(fibo(i-1))
    print(b)