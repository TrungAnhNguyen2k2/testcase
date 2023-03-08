t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b,c = min(a),max(a)
    dem =0
    for i in range(b,c+1):
        if i not in a:
            dem +=1
    print(dem)