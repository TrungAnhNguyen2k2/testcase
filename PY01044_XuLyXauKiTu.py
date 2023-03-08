s1 = list(input().lower().split())
s2 = list(input().lower().split())
s3 = set()
s4 = set()
for i in s1:
    s3.add(i)
    if i in s2:
        s4.add(i)
for j in s2:
    s3.add(j)
s3 = sorted(s3)
s4 = sorted(s4)
print(*s3)
print(*s4)