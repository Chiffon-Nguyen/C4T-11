from turtle import *
bgcolor("white")
shape("arrow")
speed(10)

#hình tam giác

color("blue","yellow")
begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()

#hình vuông
pencolor("white")
goto(50,-200)

color("blue", "yellow") #Màu đầu là pencolor, màu thứ hai là fill shape
begin_fill()
circle(50) 
end_fill()

#hình hoa 6 cánh
pencolor("white")
goto(-150,0)

for j in range (6):
    color ("green","")
    begin_fill ()
    circle(50)
    end_fill()
    right(60)


mainloop()