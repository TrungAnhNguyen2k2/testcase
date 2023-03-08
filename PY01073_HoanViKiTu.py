from itertools import permutations
a = input()
a1 = []

for i in a:
    a1.append(i)
perm=permutations(a1)
for i in perm:
    s1=""
    for j in i:
        s1 += j
    print(s1)