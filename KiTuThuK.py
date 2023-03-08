s1 = ["A","B","C",'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
N = int(input())
for j in range(N):
    n,k = map(int,input().split())
    s = ""
    for i in range(n):
        s2 = s
        s+=s1[i]
        s+=s2
    print(s[k-1])