def average(array):
    # your code goes here
    set={0}
    av = 0
    for i in array:
        set.add(i)
    for i in set:
        av += i
    av = float (av/ (len(set)-1))
    return av
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)   