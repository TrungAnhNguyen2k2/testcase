n = int(input())
for i in range(n):
    multiplication =1
    s = input()
    for i in s:
        if int(i)!=0:
            multiplication *=int(i)
    print(multiplication)