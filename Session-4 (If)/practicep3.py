print("Đây là phương trình giải phương trình bậc hai")
a = int(input("Nhập vào hệ số a"))
b = int(input("Nhập vào hệ số b"))
c = int(input("Nhập vào hệ số c"))
d = 0.5 ** (b*2 - 4*a*c) #tính delta của phương trình
if a == 0 and b == 0 and c ==0:
    print("Phương trình này có vô số nghiệm")
else:
    x1 = (b + d)/(2*a)
    x2 = (b - d)/(2*a)
    if d < 0:
        print("Phương trình này không có nghiệm")
    elif d==0:
        print("Phương trình này có 1 nghiệm duy nhất là ", x1)
    else:
        print("Phương trình có hai nghiệm là ", x1, "và ", x2)
