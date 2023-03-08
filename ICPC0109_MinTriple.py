n = int(input())
for i in range(n):
    n1= int(input())
    sum =0
    m1 = 10**19
    m2 = 10**19
    m3 = 10**19
    s=""
    a = input()
    for i in a:
        if i!=" ":
            s+=i
        if m1>int(s): m1 =int(s)
        if i ==" ":
            s =" "
        
    print(sum)