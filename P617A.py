distance = int(input())
step = 1
if distance%5==0 and distance>5: step =0
if distance>5:
    step = step +  int(distance/5)
print(step)
