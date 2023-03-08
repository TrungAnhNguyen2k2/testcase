# class SinhVien:
#     def __init__(self,msv, ten, lop):
#         self.msv = msv
#         self.ten = ten
#         self.lop = lop
#         self.diemchuyencan = 10
#         self.ghichu = ""
#     def getstr(self):
#         return self.msv + " " + self.ten + " " + self.lop + " " + str(self.diemchuyencan) + " " + self.ghichu
#     def getmsv(self):
#         return self.msv
# n = int(input())
# a = list()
# for i in range(n):
#     b = SinhVien(input(),input(),input())
#     a.append(b)
# print(a)
# diemdanh = dict()
# for i in range(n):
#     s1,s2 = input().split()
#     diemdanh[s1]= s2
    
# for i in a:
#     print(getmsv(i))
t = int(input())
m = {}
for i in range(t) :
    maSV = input()
    ten = input()
    lop = input()
    m[maSV] = [ten, lop]
for i in range(t) :
    maSV, cc = input().split()
    d = 10
    for j in cc :
        if j == 'm' : d -= 1
        elif j == 'v' : d -= 2
    if d < 0 : d = 0
    m[maSV] = m[maSV] + [d]
for i in m :
    print(i, end = ' ')
    for j in m[i] :
        print(j, end = ' ')
    if(m[i][-1] == 0) : print('KDDK')
    else : print()
