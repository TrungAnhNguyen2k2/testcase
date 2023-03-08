n = int(input())
list1 = list(map(int,input().split()))
for i in range(n-1):
    if i >= len(list1)-1: break
    elif (list1[i]+list1[i+1])%2==0:
        list1.pop(i)
        list1.pop(i)
        i-=1
        if i <0: i =0
    print(i)
    print(*list1)
print(len(list1))
