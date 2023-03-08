def thaphanoi(n,nguon,dich,trunggian):
    if n ==1:
        print(nguon,"->",dich)
        return 
    thaphanoi(n-1,nguon,trunggian,dich)
    print(nguon,"->",dich)
    thaphanoi(n-1,trunggian,dich,nguon)
n =int(input())
thaphanoi(n,"A","C","B")

