import re
s = input()
x = re.findall("[A-Za-z]",s)
y = re.findall("\d",s)
print(len(x),len(y))