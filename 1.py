b = input()
for i in range(len(b)-3,0,-3):
   b = b[:i]+","+b[i:] # vi du 19099 i se bat dau tu vi tri 2, kq: 19,099
print(b) 
# do việc sửa từ cuối lên đầu => các vị trí của kí tự ở đầu k thay đổi