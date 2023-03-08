n = int(input())
for i in range(n):
    s1 =input()
    s11 = list()
    s2 =input()
    s22 = list()
    for j in s1:
        s11.append(j)
    for j in s2:
        s22.append(j)
    # print(s11,s22)
    s11=sorted(s11)
    s22=sorted(s22)
    if (s11 ==s22) == True:
        print("Test ",i+1,":", " YES", sep="")
    else:
        print("Test ",i+1,":", " NO",sep="")