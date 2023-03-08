s1 = "I hate it"
s2 = "I hate that "
s3 = "I love it"
s4 = "I love that "
s5 =""
n = int(input())
for i in range(n-1):
    if i %2!=0:
        s5 +=s4
    else: s5+= s2
if n %2!=0:
    s5 +=s1
else: s5+= s3
print(s5)
