#ex1
first_name = str(input("Nhập vào họ"))
name = str(input("Nhập vào tên"))
print("Tên bạn là "+ first_name + " " + name)

#ex2
uppercase = str(input("Nhập gì đó"))
print(uppercase.upper())

#ex3
number = float(input("Nhập vào một số để bình phương"))
number_squared = number**2
print("Bình phương của số bạn vừa nhập: " + number_squared)

#ex4
from turtle import *
radius = float(input("Nhập bán kính của hình tròn"))
color("blue", "")
begin_fill()
circle(radius)
end_fill()

mainloop()

