import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('example.db')
n = int(input())
for i in range (n):
    # Tạo một bảng có tên là "users"
    # conn.execute('''
    #     CREATE TABLE users (
    #         id INTEGER PRIMARY KEY,
    #         username TEXT NOT NULL,
    #         password TEXT NOT NULL
    #     );
    # ''')
    # 
    # Thêm người dùng vào bảng
    username = input('Tên đăng nhập: ')
    password = input('Mật khẩu: ')

    # Lỗ hổng SQL injection ở đây: không bao vây input bằng dấu ngoặc đơn
    conn.execute('''
        INSERT INTO users (username, password) VALUES ('%s', '%s')
    ''' % (username, password))

    # Lấy tất cả các người dùng từ bảng và in ra tên đăng nhập của họ
    result = conn.execute('SELECT * FROM users')
    # print(result)
    for row in result:
        print(row)

    # Đóng kết nối
    # conn.close()