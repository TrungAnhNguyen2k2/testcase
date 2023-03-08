def checkluckynumber(s):
    ktra =1
    for i in s:
        if i !="4" and i!="7": ktra =0
    return ktra
s = input()
check =0
for i in s:
    if i =="4" or i =="7": check+=1
if checkluckynumber(str(check))==1: print("YES")
else: print("NO")