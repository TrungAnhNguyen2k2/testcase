a = list()
while len(a)<10: 
    a.extend(list(map(int,input().split())))
b = {i % 42 for i in a}
print(len(b))
