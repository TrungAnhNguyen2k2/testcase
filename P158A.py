n,k = map(int, input().split())
scores = list(map(int,input().split()))
dem = 0
for score in scores:
    if score >= scores[k-1] and score>0: dem +=1
print(dem)