print("Đây là chương trình giải phương trình bậc hai")
a = int(input("Nhâp số nguyên a"))
b = int(input("Nhập số nguyen b"))
c = int(input("Nhap so nguyen c"))
d = (b**2 - 4*a*c)**0.5
x1 = (-b - d)/(2*a)
x2 = (-b + d)/(2*a)
if d<0:
    print("Phương trình này không có nghiệm")
else:
    print("Phương trình có hai nghiệm là ", x1, "", x2)