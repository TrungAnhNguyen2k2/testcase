n = int(input())
a = list(map(float,input().split()))
max = max(a)
min = min(a)
for i in a:
    if i ==max or i ==min:
        a.remove(i)
sum =0
for i in a:
    sum+=i
print(round(sum / len(a),2))
