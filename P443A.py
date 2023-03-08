str = input()
set ={""}
# 65-90
# 97-122
for i in str:
    if ord(i) in range(65,91) or ord(i) in range(97,123): 
        set.add(i)
print (len(set)-1)