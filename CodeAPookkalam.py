##CodeAPookkalam

import turtle
from turtle import *  
bgcolor("black")
# move
speed(200)
up()
goto(0,-200)
down()

#outercircle
radius = 200
hideturtle()
color("green")
fillcolor("white")
width(3)
begin_fill()
circle(radius)
end_fill()
up()

#Gradient layers
goto(0,0)
down()
pensize(3)
outer_gradient={"#2B0303":1.414,"maroon":1.697,"red":1.979,"#F64000":2.262,"yellow":2.545,"white":2.828}
for shade in outer_gradient:
    for i in range(24):
        pensize(3)
        color(shade)
        fillcolor(shade)
        begin_fill()
        left(15)
        for sides in range(4):
            forward(radius/outer_gradient[shade])
            left(90)
        end_fill()

#second circle
up()
goto(0,-90)
down()
radius = 90
hideturtle()
color("#1A7C03")
fillcolor("#1A7C03")
width(3)
begin_fill()
circle(radius)
end_fill()
up()

#third circle
goto(0,-70)
down()
radius = 70
hideturtle()
color("#F64000")
fillcolor("#F64000")
width(3)
begin_fill()
circle(radius)
end_fill()
up()

#fourth circle
goto(0,-50)
down()
radius = 50
hideturtle()
color("yellow")
fillcolor("yellow")
width(3)
begin_fill()
circle(radius)
end_fill()
up()

#star
goto(0,0)
down()
c = ["purple","violet"]
for i in range(72):
    color(c[i%2])
    forward(i)
    left(100)
    forward(i)
    right(160)
up()

#inner circle
goto(0,-30)
down()
radius = 30
hideturtle()
color("white")
fillcolor("white")
width(3)
begin_fill()
circle(radius)
end_fill()
up()

def heart_curve():
    for i in range(200):
        right(1)
        forward(0.24)
#heart
goto(5,-28)
down()
width(3)
color("red")
fillcolor("red")
begin_fill()
left(140)
forward(35)
heart_curve()
left(120)
heart_curve()
forward(35)
end_fill()
up()

done()