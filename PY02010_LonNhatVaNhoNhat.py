while True:
    n = int(input())
    if n ==0: break
    a = [0]*n
    for i in range(n):
        a[i]= int(input())
    if max(a)!=min(a): print(min(a),max(a))
    else: print("BANG NHAU")
    