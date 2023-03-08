mod = 1000

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x} {self.y}'
    
def Tich(a, b):
    r = Pair(0, 0)
    r.x = (a.x * b.x + 5 * a.y * b.y) % mod
    r.y = (a.x * b.y + a.y *b.x) % mod
    return r

def LuyThua(a, b):
    if b == 0: return Pair(1, 0)
    if b&1: return Tich(LuyThua(a, b-1), a)
    p = LuyThua(a, b>>1)
    return Tich(p, p)

x = Pair(3, 1)
t = int(input())
for t in range(t):
    tmp = int(input())
    print(f'Case #{t+1}: ',end='')
    print(str(LuyThua(x, tmp).x * 2 % mod - 1).zfill(3))