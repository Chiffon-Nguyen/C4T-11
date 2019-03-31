#ex1
for i in range (3,13):
    print(i)

#ex2
n1 = int(input("Nhập vào một số tự nhiên khác 0"))
for k in range (0,n1+1):
    print(k)

#ex3
n2 = int(input("Nhập vào một số tự nhiên khác 0"))
for i in range (n2, 0,-1):
    print(i)

#ex4
from turtle import *
sides = int(input("How many sides would you like? "))
angle = 360 / sides
for count in range(sides):
    fd(50)
    lt(angle)

mainloop()