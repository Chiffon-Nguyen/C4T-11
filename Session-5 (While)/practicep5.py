#Chương trình yêu cầu người dùng nhập một số. Đếm số chữ số của nó
count = 0
number = int(input("Enter one number"))
while (number > 0):
    number = number //10
    count += 1
print("Your number has ", count, " digits")