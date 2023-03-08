import math


def kiemtranguyento(k):
    check =1
    if k <2:
        check =0
    for p in range(2, int(math.sqrt(k)+1)):
        if k % p == 0:
            check = 0
            break
    return check
def sum(s):
    tong=0
    for i in s:
        tong+=int(i)
    return tong
t = int(input())
for i in range(t):
    check =1
    n = input()
    m = n[::-1]
    if kiemtranguyento(int(n))==0 or kiemtranguyento(sum(n))==0 or kiemtranguyento(int(m))==0:
        check =0
    for i in n:
        if kiemtranguyento(int(i))==0: 
            check =0
            break
    if check ==1: print("Yes")
    else : print("No")

