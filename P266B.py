n, r= list(map(int, input().split()))
s1 = input()
# s2=""
# a=[""]
# for i in s1:
#     a.append(i)
while r>0:
    s1 = s1.replace("BG","GB")
    r=r-1
print(s1)