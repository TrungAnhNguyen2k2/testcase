P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s1 = input()
    if s1.strip()=="0": break
    k,s = s1.split()
    s1 =""
    k = int(k)
    for i in range(len(s)):
        for j in range(len(P)):
            if s[i]==P[j]:
                s1 += P[(j+k)%28]
    s1 = s1[::-1]
    print(s1)
