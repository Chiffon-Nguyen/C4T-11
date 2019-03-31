#ex1
number = float(input("Nhập vào một số bất kì"))
if number > 13.0:
    print("Số này lớn hơn 13")
elif number == 13.0:
    print("Số này bằng 13")
else:
    print("Số này nhỏ hơn 13")

#ex2
while True:
    even = int(input("Nhập vào một số tự nhiên"))
    if even < 0:
        print("Đây là số âm. Nhập lại")
    elif even % 2 == 0:
        print("Số này là số chẵn")
        break
    else: 
        print("Số này là số lẻ")
        break

#ex3
dayinmonth = int("Nhập vào tháng của một năm")
if dayinmonth < 1 or dayinmonth > 12:
    print("Hãy nhập số hợp lệ")
elif dayinmonth == 2:
    print("Tháng này có thể có 28 hoặc 29 ngày")
elif dayinmonth in range (1,8) and dayinmonth %2 != 0:
    print("Tháng này có 31 ngày")
elif dayinmonth in range (8,13) and dayinmonth %2 == 0:
    print("Tháng này có 31 ngày")
else:
    print("Tháng này có 30 ngày")
