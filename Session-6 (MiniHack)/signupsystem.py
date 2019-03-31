#ex3
print("Vui lòng đăng kí tài khoản")

username = str(input("Nhập tên đăng nhập"))
while True:
    email = str(input("Nhập email"))
    email_count = len(email)
    if "@" not in email or "." not in email or email_count <= 8:
        print("Email không hợp lệ. Hãy nhập lại")
    else:
        print("Email hợp lệ")
        break
while True:
    pw = str(input("Nhập mật khẩu"))
    pw_count = len(pw)
    if pw.isalpha() or pw_count <=8:
        print("Hãy nhập lại mật khẩu")
    else: 
        print("Mật khẩu hợp lệ")
        break
while True:
    repass = str(input("Nhập lại mật khẩu"))
    if pw != repass:
        print("Nhập lại không khớp. Hãy nhập lại")
    else: 
        print("Khớp mật khẩu")
        break

