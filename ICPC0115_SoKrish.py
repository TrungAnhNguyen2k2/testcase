def giaithua(s):
    if s==0:
        return 1
    return s*giaithua(s-1)

n = int(input())
for i in range(n):
    n1=input()
    tong =0
    for i in n1:
        tong += giaithua(int(i))
    # print(tong,int(n1))
    print("Yes") if tong == int(n1)else print("No")