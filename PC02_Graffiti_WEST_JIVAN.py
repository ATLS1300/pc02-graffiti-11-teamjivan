#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Jivan West
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
clear()
up()
goto(-15,112)
down()
pensize(3) #lefteye
color("red")
dot(12)

up()
goto(45,125) #righteye
down()
dot(12)

up()
goto(0,0)


 #right square
color("lawngreen")
goto(37, 110)
setheading(20)
down()
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)

up() #left square
color("lawngreen")
goto(-9,102)
setheading(20)
left(45)
down()
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)

#headbandssss
up()
goto(54,153)
setheading(90) 
color("lawngreen")
pensize(2)
down()
circle(75, 180)

up()
goto(54,145)
setheading(90) 
color("lawngreen")
pensize(1)
down()
circle(75, 180)

up()
goto(40,160)
setheading(90) 
color("red")
down()
circle(75, 180)

up()
goto(60,150)
setheading(90) 
pensize(2)
color("red")
down()
circle(75, 180)

up()
goto(45,160)
setheading(90) 
color("lawngreen")
down()
circle(75, 180)

up()
goto(53,153)
setheading(90) 
color("red")
down()
circle(75, 180)

up()
goto(45,150)
setheading(90) 
color("lawngreen")
down()
circle(75, 180)

#pentagram1
up()
goto(-125, 120)
color("red")
down()
begin_fill()
for i in range(0, 5):
    forward(200)
    right(144)
end_fill()

#pentagram2
up()
goto(170, 100)
color("red")
down()
begin_fill()
for i in range(0, 5):
    forward(200)
    right(144)
end_fill()

#jeff1
up()
goto(0,-200)
setheading(90)
down()
color("lawngreen")
style = ('JEFF', 90, 'italic')
write('JEFF <3', font=style, align='center')

#jeff2
up()
goto(-5,-195)
setheading(90)
down()
color("red")
style = ('JEFF', 90, 'italic')
write('JEFF <3', font=style, align='center')

#jeff3
up()
goto(-10,-190)
setheading(90)
down()
color("lawngreen")
style = ('JEFF', 90, 'italic')
write('JEFF <3', font=style, align='center')

#you gotta love him1
up()
goto(-10,-205)
setheading(90)
down()
color("red")
style = ('you gotta love him', 15, 'italic')
write("you gotta love him", font=style, align='center')

#you gotta love him2
up()
goto(-10,-215)
setheading(90)
down()
color("lawngreen")
style = ('you gotta love him', 15, 'italic')
write("you gotta love him", font=style, align='center')

#you gotta love him3
up()
goto(-10,-225)
setheading(90)
down()
color("red")
style = ('you gotta love him', 15, 'italic')
write("you gotta love him", font=style, align='center')








