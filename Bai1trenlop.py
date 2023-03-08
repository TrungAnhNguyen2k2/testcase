# bài 1:
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# x = int(input())
# for i in a:
#     if (x-i) in b:
#         print(i,x-i,sep=" ")
# bài 2:
n = int(input())
arr = list(input().split())
arr.sort()
s = arr[0][0]
check =1
j = 0
while check ==1:
    for i in arr:
        if i.startswith(s):
            check =1
        else:
            check =0
    if check ==1: 
        s +=arr[0][j+1]
        j +=1
    else:
        break
print(s[:-1])