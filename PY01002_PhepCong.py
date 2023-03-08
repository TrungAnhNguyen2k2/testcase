import re
s = re.sub(r'\D','',input())

if int(s[0]) + int(s[1]) == int(s[2]): print("YES")
else: print("NO")