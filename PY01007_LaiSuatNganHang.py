n = int(input())
while n>0:
    capital,interest_rate,moneyout = list(map(float, input().split()))
    year = 0
    while capital < moneyout:
        year+=1
        capital=capital*(interest_rate+100)/100
    print(year)
    n-=1