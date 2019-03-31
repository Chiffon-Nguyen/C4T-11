#Chương trình yêu cầu người dùng nhập mật khẩu. Nếu không có chữ số hoặc không trên 8 kí tự hoặc không có cả chữ hoa lẫn chữ thường thì phải nhập lại
while True:
    pw = input("Enter your password")
    pw_count = len(pw)
    if pw.isalpha() and pw.islower() and pw_count <=8:
        print("Pls reenter ur pass w/ number(s)")
    else: 
        print("Valid password")
        break
