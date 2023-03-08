n = int(input())
room=0
while n>0:
    p,q = list(map(int,input().split()))
    if (q-p)>=2: room+=1
    n-=1
print(room)