from turtle import *

# Settings
hideturtle()
speed(0)
bgcolor("black")
color("white")
pensize(10)
style = ('Arial', 30, 'normal')
screensize(1920, 1080)
setup(width=1.0, height=1.0, startx=None, starty=None)

# Huruf "O"
circle(50)

up()
goto(70, 0)
down()

# Huruf "D"
left(90)
forward(100)
right(90)
forward(20)
circle(-50, 180)
forward(20)

up()
goto(160, 0)
down()

# Huruf "I"
right(90)
forward(100)

up()
goto(180, 100)
down()

# Huruf "L"
right(180)
forward(100)
left(90)
forward(50)

up()
goto(250, 100)
down()

# Huruf "I"
right(90)
forward(100)

up()
goto(270, 50)
down()

# Huruf "O"
circle(50)

speed(3)
up()
goto(-80, 120)
down()
goto(400, 120)
goto(400, -20)
goto(-80, -20)
goto(-80, 120)
up()
color('deep pink')
goto(-90, -90)
write('Instagram: @daaaaaey', font=style)
goto(-90, -140)
write('GitHub: Loneth', font=style)
done()
