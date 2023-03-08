s = input()
check =0
for i in s:
    if i.islower() == True: check+=1
    else: check -=1
if check >=0: print(s.lower())
else: print(s.upper())