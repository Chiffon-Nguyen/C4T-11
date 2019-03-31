username = input("Nhập vào tên đăng nhập của bạn ")
if username !="techkids":
    print("You are not superuser")
else:
    password = input("Nhập vào mật khẩu của bạn ")
    if username == "techkids" and password == "codethechange":
        print("Welcome, superuser")
    else: 
        print("Invalid password")