k, n, w = list(map(int, input().split()))
money=0
for i in range (1,w+1):
    money += k*i
if money>n:
    print (money-n)
else:
    print(0)