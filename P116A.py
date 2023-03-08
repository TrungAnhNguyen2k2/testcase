n = int(input())
max = 0
people =0
while n>0:
    getout,getin = list(map(int,input().split()))
    people += (getin-getout)
    if people>max: max =people
    # print(people,max)
    n=n-1
print(max)