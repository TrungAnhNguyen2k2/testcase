class thongtinnguoi:
    def __init__(self,ten,sdt,ngaysinh ):
        self.ten = ten
        self.sdt = sdt
        self.ngaysinh = ngaysinh
        self.x = ten.split()[-1]
    def getstr(self):
        return self.ten +": "+self.sdt+" "+self.ngaysinh
ip = open("SOTAY.txt",'r')
inp = ip.read().split('\n')
a = []
while len(inp)>0:
    x = inp[0]
    inp.pop(0)
    if x[:4:] == "Ngay":  ngaysinh = x[5::]
    elif len(inp)>0:
        sdt = inp[0]
        inp.pop(0)
        a.append(thongtinnguoi(x,sdt,ngaysinh))
a=sorted(a,key = lambda x:(x.x,x.ten))
ip.close()
ot = open('DIENTHOAI.txt','w')
for i in a:
    ot.write(i.getstr()+'\n')
ot.close()