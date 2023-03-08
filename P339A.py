s = input()
a = []
st =""
for i in s:
    if i.isdigit()== True: 
        a.append(i)
a.sort()
for i in a:
    st += str(i) + "+" 
st = st.rstrip("+")
print(st)