from sys import stdin
a = list(map(int,stdin.read().split()))
n, sum1=12,sum(a)
un,s =[1]*12,[0]*4
def thu(g,indd,sum,pre):
    ans = 10**8
    if g ==3:
        s[3]= sum1-s[0]-s[1]-s[2]
        MAX = max(s)
        MIN = min(s)
        return min(ans,MAX-MIN)
    for i in range(pre,n):
        if un[i]:
            un[i]=0
            if indd==2:
                s[g]= sum+a[i]
                ans = min(ans,thu(g+1,0,0,0))
            else: 
                ans=min(ans,thu(g,indd+1,sum+a[i],i+1))
            un[i]=1
    return ans
ans = thu(0,0,0,0)
print(ans)

