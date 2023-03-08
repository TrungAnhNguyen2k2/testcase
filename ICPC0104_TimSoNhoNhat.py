import re
n = int(input())
for i in range(n):
    s = input()
    s = re.sub("\D"," ",s).strip().split()
    a = [int(i) for i in s]
    print(min(a))

