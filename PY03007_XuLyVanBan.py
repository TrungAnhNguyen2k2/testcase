import re
s =""
regex='[?.!]'
s=input()
s = list(re.split(regex,s))
s.remove('')
print(s)
for i in s:
    i = i.lower().strip()
    x = i.split()
    x[0] = x[0].title()
    print(*x, sep=" ")